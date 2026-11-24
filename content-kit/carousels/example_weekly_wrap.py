import pathlib
from playwright.sync_api import sync_playwright

# reuse the v4 wrap styles and helpers (css, mark, foot, slide)
exec(pathlib.Path("/home/claude/wrap5/build.py").read_text().split("P = lambda")[0])

W = pathlib.Path("/home/claude/wrap6")
MARK = (W / "mark.svg").read_text()
N = 10

css += """
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:34px}
.stat{background:rgba(255,255,255,.10);border-radius:18px;padding:22px 20px}
.stat b{display:block;font-size:64px;line-height:64px;font-weight:800;letter-spacing:-.04em;color:#fff}
.stat span{display:block;margin-top:10px;font-size:19px;line-height:24px;color:rgba(255,255,255,.88);font-weight:500}
.trio{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:28px}
.p img{width:100%;aspect-ratio:1;object-fit:cover;border-radius:18px;display:block;background:#ddd}
.p b{display:block;margin-top:12px;font-size:22px;line-height:26px;font-weight:700;color:var(--forest)}
.p span{display:block;margin-top:4px;font-size:17px;line-height:23px;color:var(--ink)}
.five{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin-top:26px}
.five .f{position:relative;border-radius:14px;overflow:hidden;aspect-ratio:4/5;background:var(--forest)}
.five .f img{width:100%;height:100%;object-fit:cover;object-position:50% 20%;display:block}
.five .f i{position:absolute;left:0;right:0;bottom:0;padding:18px 8px 7px;font-style:normal;font-size:14px;font-weight:600;color:#fff;background:linear-gradient(transparent,rgba(0,0,0,.65))}
.five .f.ph{display:flex;align-items:center;justify-content:center}
.five .f.ph u{text-decoration:none;font-size:46px;font-weight:800;color:var(--gold)}
.pic{flex:none}
.lift .row b{min-width:168px}
.sc .row{font-size:20px;line-height:26px;padding:10px 0}.sc .row b{min-width:92px}.sc .row:first-child{padding-top:0}
.faces{display:flex;gap:12px;margin-top:34px}
.faces img{width:76px;height:76px;border-radius:50%;object-fit:cover;box-shadow:0 0 0 3px rgba(255,255,255,.9)}
.av{display:flex;gap:16px;align-items:center;margin-top:22px}
.av img{width:84px;height:84px;border-radius:50%;object-fit:cover;flex:none}
.av p{font-size:20px;line-height:28px}
.av p b{color:var(--forest)}
"""

P = lambda n: f"file://{W}/img/{n}.png"
S = []

faces = "".join(f'<img src="{P(n)}">' for n in ["niranjana","selladurai","navin","rithik","vidhya","sairam"])
S.append(slide(1, "Weekly wrap · Nov 16–22", f'''
<h1 class="z" style="margin-top:44px;font-size:76px;line-height:78px">A week of firsts.</h1>
<p class="lede z">First-time hosts. A first showcase. A first day for Cohort 6. And three new Teedians.</p>
<div class="stats z">
<div class="stat"><b>3</b><span>new Teedians</span></div>
<div class="stat"><b>5</b><span>joined Cohort 6</span></div>
<div class="stat"><b>5</b><span>builds shown</span></div>
</div>
<div class="faces z">{faces}</div>''', "forest"))

S.append(slide(2, "Graduation · Mon & Sun", f'''
<h1>Three new Teedians.</h1>
<p class="lede">Niranjana and Selladurai graduated on Monday, in the same call where Cohort 6 began. Navin finished Cohort 4 on Sunday.</p>
<div class="trio">
<div class="p"><img src="{P('niranjana')}"><b>Niranjana</b><span>Hosted her first Tea Kadai Talks two days later.</span></div>
<div class="p"><img src="{P('selladurai')}"><b>Selladurai</b><span>“Sonnal puriyathu, suvaithal marakathu.”</span></div>
<div class="p"><img src="{P('navin')}"><b>Navin</b><span>#1 on the Hub Hall of Fame by graduation.</span></div>
</div>'''))

S.append(slide(3, "Cohort 6 · Day 1", f'''
<h1>Day 1, and already on stage.</h1>
<p class="lede">Five people started Cohort 6 this week. On his very first Tuesday, Rithik showcased his project.</p>
<div class="five">
<div class="f"><img src="{P('rithik')}"><i>Rithik</i></div>
<div class="f"><img src="{P('vidhya')}"><i>Vidhya</i></div>
<div class="f"><img src="{P('shandhip')}"><i>Shandhip</i></div>
<div class="f"><img src="{P('vijay')}"><i>Vijay</i></div>
<div class="f ph"><u>V</u><i>Vigneas</i></div>
</div>
<div class="card" style="background:var(--gold-soft)"><p style="font-size:22px;line-height:32px">English Pesalam Vaanga was meant to end at 7:30. <b style="color:var(--gold-text)">Rithik and his buddy Vidhya talked till 8.</b></p></div>'''))

S.append(slide(4, "Showcase Day · Tue, Nov 17", f'''
<h1>Five builds, one Tuesday.</h1>
<p class="lede" style="margin-top:12px">Glory hosted. Rithik showed CareQueue, his hospital queue app, on Day 1.</p>
<div class="pic" style="height:206px;margin-top:20px"><img src="{P('carequeue')}" style="object-position:0 62%"></div>
<div class="card sc" style="margin-top:18px;padding:16px 26px"><div class="row"><b>Tazim</b><span>A WhatsApp AI assistant that books meetings.</span></div><div class="row"><b>Sujay</b><span>An ML model that catches DNS data leaks.</span></div><div class="row"><b>Shifan</b><span>All your Google Classroom files in one click.</span></div><div class="row"><b>Navin</b><span>A DevSecOps project hunting security gaps.</span></div></div>'''))

S.append(slide(5, "Tea Kadai Talks · Wed, Nov 18", f'''
<h1 style="font-size:54px;line-height:58px">Use AI to sharpen your thinking. Not to skip it.</h1>
<div class="av"><img src="{P('sairam')}"><p>Mentor <b>Sairam Durairajan</b>, aerospace research scholar at IIT Madras. <b>Niranjana</b> hosted, for the first time.</p></div>
<div class="card"><div class="steps"><div class="step"><i>1</i>Know every line you ship: the logic, the syntax, the memory.</div><div class="step"><i>2</i>Why before what. Maths and physics come first.</div><div class="step"><i>3</i>Two roads to IIT after B.Tech: GATE, or research with a professor.</div></div></div>
<div class="card" style="background:var(--gold-soft);margin-top:16px"><p style="font-size:21px;line-height:30px"><b style="color:var(--gold-text)">This week's check:</b> from 1 to 10, how well do you really use AI?</p></div>'''))

S.append(slide(6, "Builder of the week", '''
<h1>Built between classes and a long commute.</h1>
<p class="lede">Kumaran from Cohort 4 kept shipping all week.</p>
<div class="card"><div class="row"><b>LinkShield</b><span>A Chrome extension in just two files. Hover on a link and it flags short URLs, raw IPs and lookalike phishing sites.</span></div><div class="row"><b>Freefall</b><span>A portfolio you fall through as you scroll, with live sound that speeds up with you.</span></div><div class="row"><b>A motor</b><span>Built an electric motor from scratch in his internship.</span></div></div>
<p class="cap" style="font-size:20px">His first browser extension. Same night, it was working.</p>'''))

S.append(slide(7, "Old meets new", '''
<p class="big z" style="margin-top:52px;font-size:88px;line-height:90px">Audacity.</p>
<p class="lede z" style="margin-top:22px">Sujay met Abinandhan, one of our OGs, at SRM University. He joined YCS in his second year of college. This is the one word Sujay took home.</p>
<p class="q z" style="margin-top:34px;color:var(--ink);font-size:30px;line-height:40px">“Taking a risk is what you did, and the world gave that action a name.”</p>
<p class="who z" style="color:var(--ink);font-size:20px">Sujay, to Abinandhan</p>
<p class="z" style="margin-top:26px;font-size:20px;line-height:28px">His article is coming soon.</p>''', "gold"))

S.append(slide(8, "Community · Lifting each other", '''
<h1>Lifting each other up.</h1>
<div class="card lift"><div class="row"><b>Tazim</b><span>Shared Navin's before-and-after story with everyone.</span></div><div class="row"><b>Navin</b><span>Introduced his buddy Hanif on the community page.</span></div><div class="row"><b>Vishnuvarthan</b><span>Shared a line worth keeping: “Don't build your career around a programming language. Build it around engineering fundamentals.”</span></div><div class="row"><b>GSthina</b><span>Put our students on a map of Tamil Nadu.</span></div></div>
<p class="cap" style="font-size:20px">The map and everyone's portfolios: yourcollegesenior.com. Not there yet? Make yours public on the Hub.</p>'''))

S.append(slide(9, "GSthina's ask", '''
<h1 class="z">Every Teedian, a cohort graduate.</h1>
<p class="lede z" style="font-size:22px;line-height:31px">“If you complete these 30 days, something in you will shift, even a small one.” Pick a cohort, finish it, bring your friends.</p>
<div class="card z"><div class="row"><b>Mon, Nov 30</b><span>Cohort 7 begins</span></div><div class="row"><b>Mon–Fri, 7 PM</b><span>English Pesalam Vaanga</span></div><div class="row"><b>Tue, 8 PM</b><span>Showcase Day</span></div><div class="row"><b>Wed, 8 PM</b><span>Tea Kadai Talks</span></div><div class="row"><b>End of Nov</b><span>Demo Day</span></div></div>
<p class="z" style="margin-top:18px;font-size:19px;font-weight:600">Join at app.teedians.in/activities</p>''', "forest"))

names = ["Niranjana", "Selladurai", "Navin", "Glory", "Rithik", "Vidhya", "Vigneas", "Vijay", "Shandhip", "Tazim",
         "Sujay", "Shifan", "Kumaran", "Srisahana", "Abinandhan", "Vishnuvarthan", "Hanif"]
chips = "".join(f'<span class="chip">{n}</span>' for n in names) + '<span class="chip g">Sairam</span><span class="chip g">GSthina</span>'
S.append(slide(10, "Thank you", f'''
<h1>You made the week.</h1>
<div class="card"><div class="chips">{chips}</div></div>
<p class="lede">And everyone who did something for the first time.</p>'''))

html = f"<!doctype html><meta charset=utf-8><style>{css}</style><body>{''.join(S)}</body>"
(W / "wrap.html").write_text(html)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 720, "height": 900}, device_scale_factor=2)
    pg.goto("file://" + str(W / "wrap.html")); pg.wait_for_timeout(1200)
    pg.pdf(path=str(W / "Teedians_Weekly_Wrap_Nov16-22.pdf"), width="720px", height="900px", print_background=True)
    (W / "png").mkdir(exist_ok=True)
    for i, el in enumerate(pg.query_selector_all("section.s"), 1):
        el.screenshot(path=str(W / f"png/{i:02d}.png"))
    print(pg.evaluate("""()=>[...document.querySelectorAll('section.s')].map(s=>{const f=s.querySelector('.foot').getBoundingClientRect();const k=[...s.children].filter(c=>!c.classList.contains('foot')&&!c.classList.contains('crop'));const l=k[k.length-1].getBoundingClientRect();return Math.round(f.top-l.bottom)})"""))
    print(pg.evaluate("document.fonts.check('700 64px \"Bricolage Grotesque\"')"))
    b.close()
