import pathlib
from playwright.sync_api import sync_playwright
src = pathlib.Path("/home/claude/wrap5/build.py").read_text()
exec(src.split("P = lambda")[0])          # css, mark, foot, slide from the weekly wrap (v4)
W = pathlib.Path("/home/claude/tkt"); N = 10
css += """
.grid6{display:grid;grid-template-columns:repeat(3,1fr);gap:10px 12px;margin-top:22px}
.grid6 div{display:flex;flex-direction:column;gap:6px}
.grid6 img{width:100%;aspect-ratio:1/1;object-fit:cover;display:block;border-radius:14px;background:#202124}
.grid6 span{color:#fff;font-size:15px;font-weight:600;opacity:.92}
.frame{position:relative;width:280px;height:340px;border-radius:21%;overflow:hidden;flex:none;background:#202124}
.frame img{width:100%;height:100%;object-fit:cover;object-position:50% 30%;display:block}
.frame::after{content:'';position:absolute;inset:0;border-radius:21%;box-shadow:inset 0 0 0 35px var(--exposure)}
.meet{display:flex;gap:28px;align-items:center}
.mid{margin:auto 0}.mid>h1:first-child,.mid>.big:first-child{margin-top:0!important}
.meet h2{font-size:40px;line-height:44px;font-weight:700;letter-spacing:-.03em;color:var(--forest)}
.meet p{font-size:20px;line-height:28px;margin-top:10px}
.tag{display:inline-block;font-size:17px;font-weight:600;padding:6px 12px;border-radius:8px;background:var(--gold-soft);color:var(--gold-text);margin-top:14px}
.scale{display:grid;grid-template-columns:repeat(10,1fr);gap:8px;margin-top:30px}
.scale i{aspect-ratio:1/1;border-radius:10px;background:rgba(255,255,255,.16);box-shadow:inset 0 0 0 2px rgba(255,255,255,.35);display:flex;align-items:center;justify-content:center;font-style:normal;font-weight:700;font-size:20px;color:#fff}
.scale i.on{background:#fff;color:var(--forest)}
.ends{display:flex;justify-content:space-between;font-size:18px;font-weight:600;margin-top:12px;color:rgba(255,255,255,.85)}
"""
P = lambda n: f"file://{W}/img/{n}.png"
people = [("sairam", "Sairam"), ("niranjana", "Niranjana"), ("navin", "Navin"),
          ("srisahana", "Srisahana"), ("sujay", "Sujay"), ("selladurai", "Selladurai")]
grid = '<div class="grid6 z">' + "".join(f'<div><img src="{P(k)}" style="object-position:50% 30%"><span>{n}</span></div>' for k, n in people) + '</div>'
L = "Tea Kadai Talks · Wed, Nov 18"
S = []
S.append(slide(1, L, f'''
<h1 class="z" style="margin-top:26px">AI wrote your code. Can you explain it?</h1>
<p class="lede z" style="margin-top:14px">An IIT Madras researcher on the vibe coding trap, and what to do instead.</p>{grid}''', "forest"))
S.append(slide(2, "Meet the mentor", f'''
<div class="mid z">
<h1>Sairam Durairajan</h1>
<p class="lede">Research Scholar and Project Officer, Aerospace, IIT Madras. He works on defence systems and aerodynamics.</p>
<div class="chips" style="margin-top:22px"><span class="chip g">Mentor</span><span class="chip">IIT Madras</span><span class="chip">Aerospace research</span></div>
<div class="card"><p style="font-size:22px;line-height:32px"><b style="color:var(--forest)">Hosted by Niranjana,</b> her first session as host. Two days after she graduated from Cohort 3.</p></div></div>'''))
S.append(slide(3, "The trap", '''
<div class="mid z">
<h1>The vibe coding trap.</h1>
<p class="lede">AI gets you a working answer, fast. The assignment is done. The code runs.</p>
<p class="lede">But if you can't explain it, you haven't learned it. You've only copied it.</p>
<div class="card" style="background:var(--gold-soft)"><p style="font-size:22px;line-height:32px">That was the question for the night: <b style="color:var(--gold-text)">shipping fast, or understanding the core?</b></p></div></div>'''))
S.append(slide(4, "What we took home · 1", '''
<div class="mid z">
<h1>Use AI to improve your results, not to skip the thinking.</h1>
<div class="card"><div class="steps"><div class="step"><i>1</i>Know what your code does, line by line.</div><div class="step"><i>2</i>Understand the logic, the syntax and the memory it uses.</div><div class="step"><i>3</i>Then let AI make it better.</div></div></div>
<p class="cap" style="font-size:20px">Skip the understanding, and you become a copy-paste developer.</p></div>'''))
S.append(slide(5, "What we took home · 2", '''
<div class="mid z">
<p class="big z" style="margin-top:64px">A grammar checker can polish your draft.</p>
<p class="big z" style="margin-top:20px">It can't teach you to think.</p>
<p class="lede z" style="margin-top:32px">Sairam's way of putting it: AI works the same way. It refines the output, not the person writing it.</p></div>''', "gold"))
S.append(slide(6, "What we took home · 3", '''
<div class="mid z">
<h1>Why before what.</h1>
<p class="lede">That's the IIT standard, in Sairam's words. Strong maths and physics come first.</p>
<div class="card"><div class="row"><b>Semester 1</b><span>Linear algebra, from the very start.</span></div><div class="row"><b>Exams</b><span>Apply core concepts to real problems, like linking gas dynamics to an ECG.</span></div><div class="row"><b>Final year</b><span>A full project that brings it all together.</span></div></div></div>'''))
S.append(slide(7, "What we took home · 4", '''
<div class="mid z">
<h1>There's more than one road to IIT.</h1>
<p class="lede">Missed JEE? It isn't the end of the road.</p>
<div class="card"><div class="row"><b>GATE</b><span>An M.Tech after your B.Tech, with far less competition than JEE.</span></div><div class="row"><b>Research</b><span>Approach a professor with a research proposal. It can lead to a thesis-based master's.</span></div></div></div>'''))
S.append(slide(8, "Then the room went quantum", '''
<div class="mid z">
<h1>Then Navin brought up quantum computing.</h1>
<p class="lede">Qubits have to be cooled to near absolute zero to stay stable. Once they are, they could solve complex engineering problems in a fraction of a second.</p>
<div class="card"><p style="font-size:22px;line-height:32px"><b style="color:var(--forest)">Navin wants to host a quantum computing event.</b> Want in? Comment "quantum".</p></div></div>'''))
scale = "".join(f'<i>{k}</i>' for k in range(1, 11))
S.append(slide(9, "Your turn", f'''
<div class="mid z"><h1>How well do you actually use AI?</h1>
<p class="lede">Everyone in the room rated themselves, mentor included. Your turn.</p>
<div class="scale">{scale}</div>
<div class="ends"><span>1 · vaguely</span><span>10 · effectively</span></div>
<p class="lede" style="margin-top:28px">Drop your number in the comments.</p></div>''', "forest"))
names = ["Srisahana", "Navin", "Tazim", "Sujay", "Selladurai"]
chips = '<span class="chip g">Sairam · mentor</span><span class="chip g">Niranjana · host</span>' + "".join(f'<span class="chip">{n}</span>' for n in names)
S.append(slide(10, "Thank you", f'''
<div class="mid z">
<h1>Bring one question.</h1>
<p class="lede">Tea Kadai Talks, every Wednesday at 8 PM. A mentor, a cup of tea and the questions you'd feel silly asking anyone else.</p>
<div class="card"><div class="chips">{chips}</div></div>
<span class="btn">Join this Wednesday</span><p style="margin-top:12px;font-size:17px;color:var(--muted)">app.teedians.in/activities</p></div>'''))

html = f"<!doctype html><meta charset=utf-8><style>{css}</style><body>{''.join(S)}</body>"
(W / "tkt.html").write_text(html)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 720, "height": 900}, device_scale_factor=2)
    pg.goto("file://" + str(W / "tkt.html")); pg.wait_for_timeout(1000)
    pg.pdf(path=str(W / "Tea_Kadai_Talks_Vibe_Coding_Trap.pdf"), width="720px", height="900px", print_background=True)
    (W / "png").mkdir(exist_ok=True)
    for f in (W / "png").glob("*.png"): f.unlink()
    for i, el in enumerate(pg.query_selector_all("section.s"), 1):
        el.screenshot(path=str(W / f"png/{i:02d}.png"))
    print(pg.evaluate("""()=>[...document.querySelectorAll('section.s')].map(s=>{const f=s.querySelector('.foot').getBoundingClientRect();const k=[...s.children].filter(c=>!c.classList.contains('foot')&&!c.classList.contains('crop'));const l=k[k.length-1].getBoundingClientRect();return Math.round(f.top-l.bottom)})"""))
    b.close()
