"""Shared reel kit: v4 styles, entrance animations, and frame-by-frame filming into one mp4 per scene."""
import pathlib, subprocess, sys, os
from playwright.sync_api import sync_playwright

K = pathlib.Path(__file__).resolve().parent
F = K.parent / "fonts"
MARK = (K.parent / "mark.svg").read_text()
FPS = 30
FACES = "".join(f"@font-face{{font-family:'B';font-weight:{w};src:url('file://{F}/BricolageGrotesque-{w}.woff2')}}" for w in (400, 500, 600, 700, 800))
CSS = FACES + (K / "base.css").read_text().replace(
    ".bg{position:absolute;right:-330px;bottom:-300px;opacity:.10}",
    ".bg{position:absolute;right:-330px;bottom:-300px;opacity:.10;z-index:0}\n.sc>*:not(.bg){position:relative;z-index:1}")
JS = (K / "base.js.tmpl").read_text().replace("{{", "{").replace("}}", "}")

def mark(px, cls=""):
    s = MARK.replace('class="tc-logo"', f'class="tc-logo {cls}"')
    return s.replace('style="width:40px;height:40px"', f'style="width:{px}px;height:{px}px"')

def A(t, kind="up", d=0.45):
    return f'data-t="{t:.3f}" data-k="{kind}" data-d="{d}"'

def page(out_dir, scenes, body, extra_css=""):
    extra_js = """<script>{const r0=window.render;window.render=(t)=>{r0(t);for(const el of document.querySelectorAll('[data-count]')){const [a,b,n]=el.dataset.count.split(',').map(Number);const p=Math.max(0,Math.min(1,(t-a)/(b-a)));const q=1-Math.pow(1-p,3);el.textContent=Math.round(n*q).toLocaleString('en-IN')}}}</script>"""
    total = scenes[-1][2]
    js = JS.replace("{SC[-1][2]}", f"{total}")
    html = f"<!doctype html><meta charset=utf-8><style>{CSS}{extra_css}</style><body><div class='prog' id='prog'></div>{body}{js}{extra_js}</body>"
    (out_dir / "reel.html").write_text(html)

def film(out_dir, scenes, names=None, checks=None):
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
        pg.goto("file://" + str(out_dir / "reel.html")); pg.wait_for_timeout(800)
        pg.evaluate("document.fonts.ready")
        if checks:
            for t in checks:
                pg.evaluate(f"render({t})"); pg.screenshot(path=str(out_dir / f"check_{t:05.2f}.jpg"), type="jpeg", quality=80)
            b.close(); return
        for n, s, e in scenes:
            if names and n not in names: continue
            frames = round((e - s) * FPS)
            tmp = out_dir / f"scene_{n}.tmp.mp4"
            ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
                                   "-c:v", "libx264", "-crf", "18", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-r", str(FPS), str(tmp)],
                                  stdin=subprocess.PIPE)
            for f in range(frames):
                pg.evaluate(f"render({s + f / FPS})")
                ff.stdin.write(pg.screenshot(type="jpeg", quality=92))
            ff.stdin.close()
            if ff.wait() == 0: os.replace(tmp, out_dir / f"scene_{n}.mp4")
            else: sys.exit("ffmpeg failed on " + n)
        b.close()

def join(out_dir, scenes, final_name):
    (out_dir / "list.txt").write_text("".join(f"file 'scene_{n}.mp4'\n" for n, _, _ in scenes))
    total = scenes[-1][2]
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(out_dir / "list.txt"), "-c", "copy", str(out_dir / "video.mp4")], check=True)
    # silent audio track so every app accepts it; the music gets added in Instagram
    tmp = out_dir / (final_name + ".tmp.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(out_dir / "video.mp4"), "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
                    "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "128k", "-t", f"{total}", "-movflags", "+faststart", str(tmp)], check=True)
    os.replace(tmp, out_dir / (final_name + ".mp4"))

def run(out_dir, scenes, final_name):
    a = sys.argv[1:]
    if a and a[0] == "check": film(out_dir, scenes, checks=[float(x) for x in a[1:]])
    else:
        film(out_dir, scenes, names=a or None); join(out_dir, scenes, final_name); print("done", final_name)
