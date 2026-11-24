"""Reel: group discussion tips from our GD practice at Office Hours (4 Nov)."""
import sys, pathlib
sys.path.insert(0, "/home/claude/reels")
from kit import A, mark, page, run

R = pathlib.Path("/home/claude/reels/gd")
SC = [("hook", 0.0, 2.8), ("t1", 2.8, 7.0), ("t2", 7.0, 11.2), ("t3", 11.2, 15.4), ("recap", 15.4, 18.6), ("cta", 18.6, 22.2)]
S = {n: (a, b) for n, a, b in SC}
css = """
.tw{font-size:120px;line-height:124px;font-weight:800;letter-spacing:-.045em}
.tip{font-size:104px;line-height:108px;font-weight:800;letter-spacing:-.04em;margin-top:40px}
.sub{margin-top:50px;font-size:52px;line-height:66px;font-weight:500}
.quote{margin-top:44px;display:inline-block;background:#fff;color:var(--ink);border-radius:28px;padding:30px 40px;font-size:50px;line-height:62px;font-weight:600}
"""
def tip(id_, theme, n, title, sub, extra=""):
    a, b = S[id_]
    bg = {"forest": f'<div class="bg">{mark(1100,"white")}</div>', "gold": f'<div class="bg" style="opacity:.12">{mark(1100,"inkm")}</div>'}.get(theme, "")
    numc = "var(--gold)" if theme == "forest" else ("var(--ink)" if theme == "gold" else "var(--gold)")
    tc = "" if theme != "cream" else ' class="forest-t"'
    lines = "".join(f'<span {A(a+0.25+0.25*i,"up",0.4)} style="display:block">{w}</span>' for i, w in enumerate(title))
    return f'''<section class="sc {theme}" id="{id_}" data-s="{a}" data-e="{b}">{bg}
  <div {A(a,'pop',0.4)} class="num" style="color:{numc}">{n}</div>
  <p class="tip"><span{tc}>{lines}</span></p>
  <p {A(a+1.2,'up',0.45)} class="sub">{sub}</p>{extra.format(t=A(a+2.0,'pop',0.45)) if extra else ''}
</section>'''

a, b = S["hook"]
body = [f'''<section class="sc forest" id="hook" data-s="{a}" data-e="{b}"><div class="bg">{mark(1100,'white')}</div>
  <div {A(a,'fade',0.3)}><span class="pill">Placement season</span></div>
  <p class="tw" style="margin-top:70px"><span {A(a+0.1,'up',0.4)} style="display:block">Your first GD</span><span {A(a+0.45,'up',0.4)} style="display:block">in placements?</span></p>
  <p {A(a+1.3,'pop',0.4)} class="lede gold-t" style="margin-top:70px;font-size:68px;line-height:80px;font-weight:800">Do these 3 things.</p>
</section>''',
 tip("t1", "cream", "1", ["Open it,", "or close it."], "Starting first, or summing it up at the end, shows leadership. Recruiters notice both."),
 tip("t2", "gold", "2", ["One real", "example beats", "ten opinions."], "Tell a short story from your own life. It's what people remember."),
 tip("t3", "forest", "3", ["Talk to the", "group, not the", "moderator."], "Build on what others said.", '<p {t}><span class="quote">"Adding to that point..."</span></p>')]
a, b = S["recap"]
body.append(f'''<section class="sc cream" id="recap" data-s="{a}" data-e="{b}">
  <div {A(a,'fade',0.3)}><span class="pill">Save this for placement season</span></div>
  <div class="card" style="margin-top:70px">
    <div {A(a+0.2,'up',0.4)} class="tick"><b></b>Open it, or close it.</div>
    <div {A(a+0.5,'up',0.4)} class="tick"><b></b>Bring one real example.</div>
    <div {A(a+0.8,'up',0.4)} class="tick"><b></b>Build on the group.</div>
  </div>
</section>''')
a, b = S["cta"]
body.append(f'''<section class="sc forest" id="cta" data-s="{a}" data-e="{b}"><div class="bg">{mark(1100,'white')}</div>
  <h2 style="font-size:116px;line-height:114px"><div {A(a+0.1,'up',0.4)}>We practise</div><div {A(a+0.35,'up',0.4)} class="gold-t">GDs live.</div></h2>
  <p {A(a+0.9,'up',0.4)} class="lede" style="margin-top:44px;font-size:52px;line-height:64px">Students run the room, and everyone gets 90 seconds.</p>
  <div {A(a+1.5,'fade',0.4)} style="margin-top:90px;display:flex;align-items:center;gap:26px">{mark(96,'white')}<div><div style="font-size:42px;font-weight:700">Teedians Community</div><div style="font-size:32px;font-weight:500;opacity:.85;margin-top:6px">Tea Kadai Talks · every Wednesday, 8 PM</div></div></div>
</section>''')
page(R, SC, "\n".join(body), css)
run(R, SC, "Teedians_Reel_GD_3_Things")
