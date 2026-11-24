"""Reel: 'Missed IIT after JEE? Two more doors.' from Tea Kadai Talks with Sairam (18 Nov).
1080x1920, 30 fps. Each scene is filmed frame by frame from one HTML page and piped into ffmpeg."""
import pathlib, subprocess, sys, os, json
from playwright.sync_api import sync_playwright

R = pathlib.Path("/home/claude/reel1")
F = pathlib.Path("/home/claude/ds/project/fonts")
MARK = pathlib.Path("/home/claude/wrap5/mark.svg").read_text()
FPS = 30
BEAT = 0.6
# scene: (name, start, end)
SC = [("hook", 0.0, 3.6), ("mentor", 3.6, 6.6), ("door1", 6.6, 12.6), ("door2", 12.6, 18.6), ("prep", 18.6, 23.4), ("cta", 23.4, 29.4)]
T = {n: s for n, s, e in SC}

def mark(px, cls=""):
    s = MARK.replace('class="tc-logo"', f'class="tc-logo {cls}"')
    return s.replace('style="width:40px;height:40px"', f'style="width:{px}px;height:{px}px"')

faces = "".join(f"@font-face{{font-family:'B';font-weight:{w};src:url('file://{F}/BricolageGrotesque-{w}.woff2')}}" for w in (400, 500, 600, 700, 800))
css = faces + """
:root{--forest:#17703C;--gold:#F5B400;--cream:#F4EFE2;--ink:#1A1A17;--muted:#67665F;--chart1:#1F9D55;--track:#E3DFD3;--goldt:#8A6400}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1920px;overflow:hidden;background:#000;font-family:'B',sans-serif}
.sc{position:absolute;inset:0;display:none;flex-direction:column;justify-content:center;overflow:hidden;padding:200px 96px 360px}
.forest{background:var(--forest);color:#fff}.cream{background:var(--cream);color:var(--ink)}.gold{background:var(--gold);color:var(--ink)}
.tc-logo{--lg:#17703C;--ly:#F5B400;--lk:#1A1A17;--lo:#DFA000;display:block}
.tc-logo.white{--lg:#fff;--ly:#fff;--lk:#fff;--lo:#fff}.tc-logo.inkm{--lg:#1A1A17;--ly:#1A1A17;--lk:#1A1A17;--lo:#1A1A17}
.bg{position:absolute;right:-330px;bottom:-300px;opacity:.10;z-index:0}
.sc>*:not(.bg){position:relative;z-index:1}
.brand{display:flex;align-items:center;gap:18px;font-size:30px;font-weight:600}
.pill{display:inline-flex;align-items:center;height:62px;padding:0 26px;border-radius:31px;font-size:28px;font-weight:600}
.forest .pill{background:rgba(255,255,255,.14);color:#fff}.cream .pill{background:#E3F1E7;color:var(--forest)}.gold .pill{background:rgba(26,26,23,.10);color:var(--ink)}
.a{will-change:transform,opacity}
h1{font-size:150px;line-height:146px;font-weight:800;letter-spacing:-.045em}
h2{font-size:104px;line-height:104px;font-weight:800;letter-spacing:-.04em}
.lede{font-size:46px;line-height:60px;font-weight:500}
.gold-t{color:var(--gold)}.forest-t{color:var(--forest)}
.num{font-size:300px;line-height:240px;font-weight:800;letter-spacing:-.06em;color:var(--gold)}
.bars{margin-top:70px;display:grid;gap:54px}
.bl{display:flex;justify-content:space-between;align-items:baseline;font-size:44px;font-weight:700;margin-bottom:16px}
.bl span{font-size:34px;font-weight:500;color:var(--muted)}
.track{height:64px;border-radius:16px;background:var(--track);overflow:hidden}
.fill{height:100%;border-radius:16px;width:0}
.steps{margin-top:70px;display:grid;gap:34px}
.step{display:flex;gap:30px;align-items:flex-start;background:rgba(255,255,255,.12);border-radius:28px;padding:36px 36px;font-size:46px;line-height:58px;font-weight:600}
.step i{flex:none;width:72px;height:72px;border-radius:18px;background:var(--gold);color:var(--ink);font-style:normal;font-weight:800;font-size:40px;display:flex;align-items:center;justify-content:center;margin-top:-6px}
.photo{width:420px;height:420px;border-radius:50%;object-fit:cover;box-shadow:0 0 0 12px #fff,0 0 0 24px var(--gold);display:block}
.card{background:#fff;border-radius:32px;padding:44px 48px;color:var(--ink)}
.tick{display:flex;gap:26px;align-items:center;font-size:48px;line-height:60px;font-weight:600;padding:24px 0;border-top:3px solid rgba(26,26,23,.12)}
.tick:first-child{border-top:0;padding-top:0}.tick:last-child{padding-bottom:0}
.tick b{flex:none;width:22px;height:22px;border-radius:6px;background:var(--forest)}
.prog{position:absolute;left:0;top:0;height:10px;background:var(--gold);z-index:9}
.choice{display:flex;gap:30px;margin-top:70px}
.choice div{flex:1;border-radius:32px;background:#fff;color:var(--ink);padding:40px 36px}
.choice b{display:block;font-size:150px;line-height:130px;font-weight:800;color:var(--forest);letter-spacing:-.05em}
.choice span{display:block;margin-top:16px;font-size:40px;line-height:50px;font-weight:600}
"""

def A(t, kind="up", d=0.45, extra=""):
    return f'data-t="{t:.3f}" data-k="{kind}" data-d="{d}" {extra}'

h, m, d1, d2, pr, ct = (T[k] for k in ("hook", "mentor", "door1", "door2", "prep", "cta"))
html = f"""<!doctype html><meta charset=utf-8><style>{css}</style><body>
<div class="prog" id="prog"></div>

<section class="sc forest" id="hook" data-s="{h}" data-e="{T['mentor']}">
  <div class="bg">{mark(1100,'white')}</div>
  <div {A(h+0.0,'fade',0.3)}><span class="pill">Tea Kadai Talks · IIT Madras</span></div>
  <h1 style="margin-top:110px"><div {A(h+0.15,'up',0.5)}>Missed IIT</div><div {A(h+0.55,'up',0.5)}>after JEE?</div></h1>
  <p class="lede" style="margin-top:90px;font-size:64px;line-height:76px;font-weight:700"><span {A(h+1.6,'pop',0.45)} style="display:inline-block" class="a gold-t">There are two more doors.</span></p>
</section>

<section class="sc cream" id="mentor" data-s="{m}" data-e="{d1}">
  <div {A(m+0.0,'fade',0.3)}><span class="pill">Tea Kadai Talks</span></div>
  <div style="margin-top:90px"><img {A(m+0.05,'pop',0.5)} class="a photo" src="file://{R}/img/sairam.png"></div>
  <h2 style="margin-top:84px;font-size:88px;line-height:92px"><div {A(m+0.35,'up',0.45)} class="a forest-t">Sairam Durairajan</div></h2>
  <p class="lede" style="margin-top:26px"><span {A(m+0.65,'up',0.45)} style="display:block">Aerospace research scholar,</span><span {A(m+0.8,'up',0.45)} style="display:block">IIT Madras</span></p>
  <p style="margin-top:44px"><span {A(m+1.15,'fade',0.4)} class="a pill" style="display:inline-flex;background:var(--gold);color:var(--ink)">Teedians mentor and your college senior</span></p>
</section>

<section class="sc cream" id="door1" data-s="{d1}" data-e="{d2}">
  <div style="display:flex;align-items:flex-end;gap:36px"><div {A(d1+0.0,'pop',0.45)} class="a num">1</div><div><div {A(d1+0.15,'fade',0.3)} style="font-size:36px;font-weight:600;color:var(--muted)">Door one</div><h2 {A(d1+0.25,'up',0.45)} class="a forest-t" style="font-size:130px;line-height:120px">GATE</h2></div></div>
  <div class="bars">
    <div {A(d1+0.6,'up',0.4)}><div class="bl">JEE <span>lakhs of students, every branch</span></div><div class="track"><div class="fill" data-bar="{d1+0.8:.3f},{d1+1.9:.3f},100" style="background:#B9B3A3"></div></div></div>
    <div {A(d1+1.9,'up',0.4)}><div class="bl" style="color:var(--forest)">GATE <span>only your own branch</span></div><div class="track"><div class="fill" data-bar="{d1+2.1:.3f},{d1+2.7:.3f},7" style="background:var(--chart1)"></div></div></div>
  </div>
  <p style="margin-top:110px;font-size:72px;line-height:82px;font-weight:800;letter-spacing:-.03em"><span {A(d1+3.3,'up',0.45)} style="display:block">Same IITs.</span><span {A(d1+3.8,'up',0.45)} style="display:block" class="a forest-t">A much smaller crowd.</span></p>
</section>

<section class="sc forest" id="door2" data-s="{d2}" data-e="{pr}">
  <div class="bg">{mark(1100,'white')}</div>
  <div style="display:flex;align-items:flex-end;gap:36px"><div {A(d2+0.0,'pop',0.45)} class="a num">2</div><div><div {A(d2+0.15,'fade',0.3)} style="font-size:36px;font-weight:600;opacity:.85">Door two</div><h2 {A(d2+0.25,'up',0.45)} style="font-size:96px;line-height:96px">Research</h2></div></div>
  <p class="lede" style="margin-top:40px;font-size:54px;line-height:66px;font-weight:600"><span {A(d2+0.5,'up',0.45)} style="display:block">A research master's (MS)</span><span {A(d2+0.65,'up',0.45)} style="display:block">at IIT, with a professor.</span></p>
  <div class="steps">
    <div {A(d2+1.5,'up',0.45)} class="a step"><i>1</i><span>Clear the written test and the interview.</span></div>
    <div {A(d2+2.6,'up',0.45)} class="a step"><i>2</i><span>Build your thesis with a professor.</span></div>
  </div>
</section>

<section class="sc gold" id="prep" data-s="{pr}" data-e="{ct}">
  <div class="bg" style="opacity:.12">{mark(1100,'inkm')}</div>
  <div {A(pr+0.0,'fade',0.3)}><span class="pill">Either door</span></div>
  <h1 style="margin-top:80px;font-size:140px;line-height:136px"><div {A(pr+0.15,'up',0.45)}>Why</div><div {A(pr+0.45,'up',0.45)}>before what.</div></h1>
  <div class="card" style="margin-top:90px">
    <div {A(pr+1.3,'up',0.45)} class="a tick"><b></b>Maths and physics first.</div>
    <div {A(pr+2.2,'up',0.45)} class="a tick"><b></b>Know every line of your code.</div>
    <div {A(pr+3.1,'up',0.45)} class="a tick"><b></b>Use AI to sharpen your thinking, not skip it.</div>
  </div>
</section>

<section class="sc forest" id="cta" data-s="{ct}" data-e="{ct+6.0}">
  <div class="bg">{mark(1100,'white')}</div>
  <h2 style="font-size:116px;line-height:114px"><div {A(ct+0.1,'up',0.45)}>Which door</div><div {A(ct+0.35,'up',0.45)}>are you taking?</div></h2>
  <div class="choice"><div {A(ct+0.9,'pop',0.45)} class="a"><b>1</b><span>GATE</span></div><div {A(ct+1.1,'pop',0.45)} class="a"><b>2</b><span>Research with a professor</span></div></div>
  <p {A(ct+1.6,'up',0.45)} class="a lede" style="margin-top:56px;font-size:52px;font-weight:700">Comment 1 or 2.</p>
  <div {A(ct+2.4,'fade',0.5)} class="a" style="margin-top:110px;display:flex;align-items:center;gap:26px">{mark(96,'white')}<div><div style="font-size:42px;font-weight:700">Teedians Community</div><div style="font-size:32px;font-weight:500;opacity:.85;margin-top:6px">Tea Kadai Talks · every Wednesday, 8 PM</div></div></div>
</section>
<script>
const TOTAL={SC[-1][2]};
const ease=p=>1-Math.pow(1-p,3), back=p=>{{const c1=1.5,c3=c1+1;return 1+c3*Math.pow(p-1,3)+c1*Math.pow(p-1,2)}};
const cl=x=>Math.max(0,Math.min(1,x));
window.render=(t)=>{{
  document.getElementById('prog').style.width=(t/TOTAL*100)+'%';
  for(const s of document.querySelectorAll('.sc')){{
    const a=+s.dataset.s,e=+s.dataset.e; s.style.display=(t>=a&&t<e)?'flex':'none';
    if(t>=a&&t<e){{ const bg=s.querySelector('.bg'); if(bg){{bg.style.transform=`scale(${{1+0.06*(t-a)/(e-a)}}) rotate(${{-3*(t-a)/(e-a)}}deg)`}} }}
  }}
  for(const el of document.querySelectorAll('[data-t]')){{
    const p=cl((t-(+el.dataset.t))/(+el.dataset.d)), k=el.dataset.k;
    if(k==='up'){{const q=ease(p);el.style.opacity=q;el.style.transform=`translateY(${{(1-q)*70}}px)`}}
    else if(k==='fade'){{el.style.opacity=ease(p);el.style.transform='none'}}
    else if(k==='pop'){{const q=p>=1?1:back(p);el.style.opacity=cl(p*2.5);el.style.transform=`scale(${{0.6+0.4*q}})`}}
  }}
  for(const el of document.querySelectorAll('[data-bar]')){{
    const [a,b,w]=el.dataset.bar.split(',').map(Number); el.style.width=(ease(cl((t-a)/(b-a)))*w)+'%';
  }}
}};
</script></body>"""
(R / "reel.html").write_text(html)

def film(names, still_times=None):
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
        pg.goto("file://" + str(R / "reel.html")); pg.wait_for_timeout(800)
        pg.evaluate("document.fonts.ready")
        if still_times:
            for t in still_times:
                pg.evaluate(f"render({t})"); pg.screenshot(path=str(R / f"check_{t:05.2f}.jpg"), type="jpeg", quality=80)
            b.close(); return
        for n, s, e in SC:
            if names and n not in names: continue
            frames = round((e - s) * FPS)
            tmp = R / f"scene_{n}.tmp.mp4"
            ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
                                   "-c:v", "libx264", "-crf", "18", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-r", str(FPS), str(tmp)],
                                  stdin=subprocess.PIPE)
            for f in range(frames):
                pg.evaluate(f"render({s + f / FPS})")
                ff.stdin.write(pg.screenshot(type="jpeg", quality=92))
            ff.stdin.close()
            if ff.wait() == 0: os.replace(tmp, R / f"scene_{n}.mp4"); print("scene", n, frames)
            else: sys.exit("ffmpeg failed on " + n)
        b.close()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "check":
        film(None, [float(x) for x in sys.argv[2:]])
    else:
        film(sys.argv[1:] if len(sys.argv) > 1 else None)
