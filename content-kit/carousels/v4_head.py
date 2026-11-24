import pathlib, re
from playwright.sync_api import sync_playwright

W = pathlib.Path(__file__).resolve().parent
F = W.parent / "fonts"
MARK = (W.parent / "mark.svg").read_text()
N = 10

def mark(px, cls="", style=""):
    s = MARK.replace('class="tc-logo"', f'class="tc-logo {cls}"')
    return s.replace('style="width:40px;height:40px"', f'style="width:{px}px;height:{px}px;{style}"')

faces = "".join(
    f"@font-face{{font-family:'Bricolage Grotesque';font-weight:{w};src:url('file://{F}/BricolageGrotesque-{w}.woff2') format('woff2')}}"
    for w in (400, 500, 600, 700, 800))

css = faces + """
:root{--forest:#17703C;--gold:#F5B400;--cream:#F4EFE2;--ink:#1A1A17;--muted:#67665F;--chart1:#1F9D55;--track:#E3DFD3;
--forest-soft:#E3F1E7;--gold-soft:#FDF3D2;--gold-text:#8A6400;--exposure:#DFA000}
*{box-sizing:border-box;margin:0;padding:0}
@page{size:720px 900px;margin:0}
body{background:#888;font-family:'Bricolage Grotesque',sans-serif;color:var(--ink);font-variant-numeric:tabular-nums}
.s{width:720px;height:900px;padding:56px 64px 52px;display:flex;flex-direction:column;position:relative;overflow:hidden;background:var(--cream);page-break-after:always}
.s.forest{background:var(--forest);color:#fff}
.s.gold{background:var(--gold);color:var(--ink)}
.z{position:relative;z-index:1}
.tc-logo{--lg:#17703C;--ly:#F5B400;--lk:#1A1A17;--lo:#DFA000;display:block;flex:none}
.tc-logo.white{--lg:#fff;--ly:#fff;--lk:#fff;--lo:#fff}
.tc-logo.inkm{--lg:#1A1A17;--ly:#1A1A17;--lk:#1A1A17;--lo:#1A1A17}
.top{display:flex;justify-content:space-between;align-items:center;font-size:18px;line-height:24px;font-weight:600}
.brand{display:flex;align-items:center;gap:12px}
.type{color:var(--forest);font-weight:600}
.forest .type{color:#fff;opacity:.85}.gold .type{color:var(--ink)}
h1{margin-top:40px;font-size:64px;line-height:68px;font-weight:700;letter-spacing:-.035em;color:var(--forest);text-wrap:balance}
.forest h1{color:#fff}.gold h1{color:var(--ink)}
.lede{margin-top:18px;font-size:24px;line-height:34px;font-weight:400;text-wrap:pretty}
.forest .lede{color:rgba(255,255,255,.88)}
.card{background:#fff;color:var(--ink);border-radius:20px;padding:24px 28px;margin-top:28px}
.row{display:flex;gap:16px;align-items:baseline;padding:12px 0;border-top:1px solid #E8E5DE;font-size:21px;line-height:28px}
.row:first-child{border-top:0;padding-top:0}.row:last-child{padding-bottom:0}
.row b{font-weight:600;color:var(--forest);min-width:132px;flex:none}
.pic{margin-top:28px;border-radius:20px;overflow:hidden;position:relative;background:#202124}
.pic img{display:block;width:100%;height:100%;object-fit:cover}
.ov{position:absolute;background:var(--forest);border-radius:12px;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff;text-align:center;padding:8px}
.ov b{font-size:26px;font-weight:700;letter-spacing:-.02em;line-height:1.05}.ov i{font-style:normal;font-size:13px;font-weight:500;margin-top:6px;opacity:.9}
.cap{font-size:18px;line-height:26px;color:var(--muted);margin-top:14px}
.q{font-size:28px;line-height:36px;font-weight:600;letter-spacing:-.01em;color:var(--forest)}
.who{font-size:17px;color:var(--muted);margin-top:8px;font-weight:500}
.big{font-size:52px;line-height:58px;font-weight:700;letter-spacing:-.03em;text-wrap:balance}
.steps{display:grid;gap:14px}
.step{display:flex;gap:16px;align-items:center;font-size:22px;line-height:28px;font-weight:500}
.step i{flex:none;width:34px;height:34px;border-radius:8px;background:var(--chart1);color:#fff;font-style:normal;font-weight:700;font-size:18px;display:flex;align-items:center;justify-content:center}
.chips{display:flex;flex-wrap:wrap;gap:10px}
.chip{font-size:21px;font-weight:600;padding:8px 14px;border-radius:8px;background:var(--forest-soft);color:var(--forest)}
.chip.g{background:var(--gold-soft);color:var(--gold-text)}
.btn{display:inline-flex;align-items:center;height:56px;padding:0 24px;border-radius:12px;background:var(--forest);color:#fff;font-size:20px;font-weight:600;align-self:flex-start;margin-top:28px}
.forest .btn{background:#fff;color:var(--forest)}
.foot{margin-top:auto;display:flex;align-items:center;gap:5px;padding-top:24px}
.foot i{width:18px;height:18px;border-radius:5px;background:var(--track);display:block}
.foot i.on{background:var(--chart1)}
.foot i.now{background:transparent;box-shadow:inset 0 0 0 3px var(--exposure)}
.forest .foot i{background:rgba(255,255,255,.22)}.forest .foot i.on{background:#fff}.forest .foot i.now{background:transparent;box-shadow:inset 0 0 0 3px var(--gold)}
.gold .foot i{background:rgba(26,26,23,.15)}.gold .foot i.on{background:var(--ink)}.gold .foot i.now{background:transparent;box-shadow:inset 0 0 0 3px var(--ink)}
.sw{margin-left:auto;font-size:18px;font-weight:600;color:var(--forest);display:flex;gap:8px;align-items:center}
.forest .sw{color:#fff}.gold .sw{color:var(--ink)}
.crop{position:absolute;right:-210px;bottom:-230px;z-index:0}
"""

ARROW = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

def foot(i):
    sq = "".join(f'<i class="{"on" if k < i else ("now" if k == i else "")}"></i>' for k in range(1, N + 1))
    return f'<div class="foot z">{sq}<span class="sw">{"Swipe" if i < N else "Share it"} {ARROW}</span></div>'

def slide(i, label, body, theme=""):
    lc = {"forest": "white", "gold": "inkm"}.get(theme, "")
    crop = ""
    if theme == "forest":
        crop = f'<div class="crop" style="opacity:.10">{mark(620, "white")}</div>'
    elif theme == "gold":
        crop = f'<div class="crop" style="opacity:.12">{mark(620, "inkm")}</div>'
    return (f'<section class="s {theme}">{crop}<div class="top z"><span class="brand">{mark(40, lc)}Teedians Community</span>'
            f'<span class="type">{label}</span></div>{body}{foot(i)}</section>')

