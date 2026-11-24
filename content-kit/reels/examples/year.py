"""Reel: 'I feel like we haven't done much this year...' (trend format) with Teedians' 2026 in numbers from the Hub."""
import sys, pathlib
sys.path.insert(0, "/home/claude/reels")
from kit import A, mark, page, run

R = pathlib.Path("/home/claude/reels/year")
IMG = "/home/claude/wrap6/img"
STATS = [  # (number, line, theme) — from the Teedians Hub, 25 Nov 2026
    (262, "people joined the Hub", "forest"),
    (6, "cohorts started their 30 days", "cream"),
    (363, "daily challenges done", "gold"),
    (47, "projects shown on Showcase Day", "forest"),
    (141, "times we practised English together", "cream"),
    (17, "portfolios went live", "gold"),
    (16, "mentors who are your college seniors", "forest"),
]
SC = [("open", 0.0, 2.7)]
t = 2.7
for i, _ in enumerate(STATS):
    SC.append((f"s{i}", t, t + 1.35)); t += 1.35
SC += [("faces", t, t + 1.8), ("turn", t + 1.8, t + 3.9), ("cta", t + 3.9, t + 6.6)]
S = {n: (a, b) for n, a, b in SC}

css = """
.stat{font-size:330px;line-height:290px;font-weight:800;letter-spacing:-.06em}
.forest .stat{color:var(--gold)}.cream .stat{color:var(--forest)}.gold .stat{color:var(--ink)}
.sl{margin-top:40px;font-size:72px;line-height:80px;font-weight:700;letter-spacing:-.03em}
.mosaic{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:60px}
.mosaic img{width:100%;aspect-ratio:1;object-fit:cover;border-radius:28px;display:block}
.tw{font-size:96px;line-height:104px;font-weight:800;letter-spacing:-.04em}
"""
body = []
a, b = S["open"]
body.append(f'''<section class="sc cream" id="open" data-s="{a}" data-e="{b}">
  <div {A(a,'fade',0.3)}><span class="pill">Teedians · 2026</span></div>
  <p class="tw" style="margin-top:70px"><span {A(a+0.1,'up',0.4)} style="display:block">I feel like</span><span {A(a+0.45,'up',0.4)} style="display:block">we haven't</span><span {A(a+0.8,'up',0.4)} style="display:block">done much</span><span {A(a+1.15,'up',0.4)} style="display:block" class="forest-t">this year...</span></p>
</section>''')
for i, (n, line, theme) in enumerate(STATS):
    a, b = S[f"s{i}"]
    bg = f'<div class="bg"{" style=opacity:.12" if theme == "gold" else ""}>{mark(1100, "white" if theme == "forest" else ("inkm" if theme == "gold" else ""))}</div>' if theme != "cream" else ""
    body.append(f'''<section class="sc {theme}" id="s{i}" data-s="{a}" data-e="{b}">{bg}
  <div {A(a,'pop',0.35)} class="stat" data-count="{a:.3f},{a+0.7:.3f},{n}">0</div>
  <p {A(a+0.12,'up',0.35)} class="sl">{line}</p>
</section>''')
a, b = S["faces"]
faces = ["niranjana", "selladurai", "navin", "rithik", "vidhya", "shandhip", "sairam", "vijay", "coldbox"][:6]
body.append(f'''<section class="sc forest" id="faces" data-s="{a}" data-e="{b}"><div class="bg">{mark(1100,'white')}</div>
  <p {A(a,'up',0.35)} class="sl" style="margin-top:0">and a lot of new people</p>
  <div class="mosaic">{"".join(f'<img {A(a+0.08*k,"pop",0.35)} src="file://{IMG}/{f}.png">' for k, f in enumerate(faces))}</div>
</section>''')
a, b = S["turn"]
body.append(f'''<section class="sc gold" id="turn" data-s="{a}" data-e="{b}"><div class="bg" style="opacity:.12">{mark(1100,'inkm')}</div>
  <p class="tw"><span {A(a+0.1,'up',0.4)} style="display:block">...okay.</span><span {A(a+0.6,'up',0.4)} style="display:block">Maybe we did</span><span {A(a+0.95,'up',0.4)} style="display:block">a few things.</span></p>
</section>''')
a, b = S["cta"]
body.append(f'''<section class="sc forest" id="cta" data-s="{a}" data-e="{b}"><div class="bg">{mark(1100,'white')}</div>
  <p {A(a+0.05,'fade',0.3)}><span class="pill">Your turn</span></p>
  <h2 style="margin-top:60px;font-size:112px;line-height:112px"><div {A(a+0.15,'up',0.4)}>Cohort 7</div><div {A(a+0.4,'up',0.4)} class="gold-t">starts 30 Nov.</div></h2>
  <p {A(a+0.9,'up',0.4)} class="lede" style="margin-top:40px;font-size:50px;line-height:62px">30 days. 15 minutes a day. Figuring out life beyond college, together.</p>
  <div {A(a+1.4,'fade',0.4)} style="margin-top:80px;display:flex;align-items:center;gap:26px">{mark(96,'white')}<div style="font-size:42px;font-weight:700">Teedians Community</div></div>
</section>''')
page(R, SC, "\n".join(body), css)
run(R, SC, "Teedians_Reel_Year_In_Numbers")
