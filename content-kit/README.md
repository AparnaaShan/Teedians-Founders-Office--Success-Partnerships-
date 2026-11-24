# Teedians content kit

Everything needed to make Teedians reels, carousels and the weekly wrap in the v4 design system, and to schedule them on Buffer.

## Goal

150,000 impressions a month across Instagram (@teedians.community) and the Teedians LinkedIn page.
Baseline, 27 Oct to 24 Nov 2026: about 8,000 (Instagram 4,323 views, LinkedIn 2,651 impressions, X 1,051).
What works best: real stories with faces and names (events, weekly wraps, mentor notes). Single-image tips do poorly. Reels reach people who don't follow us yet.

## Weekly cadence

| Day | Instagram | LinkedIn |
|---|---|---|
| Mon, ~8:40 AM | Weekly wrap carousel (Mon to Sun, story style) | Weekly wrap as a PDF document |
| Tue, ~7 to 8 PM | Reel (reminder, sound added in the app) | |
| Wed, ~9 AM | | A reel as native video, with music |
| Thu, ~7 to 8 PM | Reel (reminder) | |
| Fri, ~9 AM | Carousel: mentor notes or tips | A reel as native video, with music |
| Sat, ~7 to 8 PM | Reel (reminder) | |

Use minutes that aren't on the hour or half hour (7:12, 7:18, 8:42).

## Brand and wording rules

- Colours: forest #17703C, gold #F5B400, cream #F4EFE2, ink #1A1A17. Font: Bricolage Grotesque (fonts/). Logo: mark.svg.
- Short sentences, human tone. Say "life beyond college" and "semester" (never "term").
- People in a cohort are not "Teedians" yet. They become Teedians when they graduate.
- Mentors are "Teedians mentor and your college senior". The founder is "GSthina" in public posts.
- Name the hosts and participants. Thank them.
- Never include personal feedback, private struggles, phone numbers or emails. Only use what people already shared with the community.
- Never change anyone's face. Only crop and scale. In Cohort 6 Meet screenshots Vijay has no shirt on: use the tee-edited tile from weekly-wraps/nov16-22 (slide 3) or leave him out.
- Don't put numbers on screen that you can't check. If a transcript is garbled, keep claims general.

## Sources

- Fathom: community sessions only (Office Hours, Tea Kadai Talks, Showcase Day, Casual connect, cohort onboarding and graduation). Never use 1:1s, Founder ops syncs, coaching or any private "Impromptu" meeting.
- Slack: #your-college-main-gate, #cohort-graduates, #teedians-cohort-* (public community posts).
- Teedians Hub (Supabase llazagnvlzbnruafcdlu, read-only): timeline_entries (proof of work, graduations, member posts), showcases, cohorts, members.
- Buffer metrics from the last week, to double down on what worked.

## Reels (reels/)

- 1080 x 1920, 30 fps, 15 to 30 seconds. The hook lands in the first 2 seconds. Keep text out of the top 200 px and bottom 360 px.
- Write a build script like examples/*.py: define scenes, build the page with kit.page(), then kit.run(). `python3 build.py check 2.5 6.0` draws still frames to look at first; `python3 build.py` films every scene and joins them into one mp4 with a silent audio track.
- Instagram gets the silent version: the trending sound is added in the Instagram app.
- LinkedIn gets a version with music: `python3 music.py <duration> <cut1,cut2,...> music.wav`, then mux it in with ffmpeg (`-c:v copy`, `loudnorm=I=-15:TP=-1.5`).
- Never download or embed songs from the internet.

## Carousels (carousels/)

- 720 x 900 slides rendered at 2x (1440 x 1800). v4_head.py holds the styles and slide helpers; see example_weekly_wrap.py and example_tea_kadai_talks.py.
- Instagram: PNG or JPG slides. LinkedIn: the same slides as one PDF document.

## Hosting media for Buffer

Commit media to this repo and use raw links:
`https://raw.githubusercontent.com/AparnaaShan/Teedians-Founders-Office--Success-Partnerships-/main/<path>`
Reels go under instagram/reels/<yyyy-mm-dd-slug>/, weekly wraps under weekly-wraps/<monDD-DD>/.

## Buffer

- Organization 6ad79d92b741e310cfb32843. Channels: Instagram 6aea13a8e29c69a1714d407e, LinkedIn page 6aeb7a38e29c69a171610779, X 6aeb6c91e29c69a17160307b.
- Instagram reels: schedulingType "notification" (Buffer reminds Aparnaa to post, so she can add a trending sound), metadata.instagram type "reel", shouldShareToFeed true.
- Carousels and LinkedIn posts: schedulingType "automatic".
- Free plan: about 10 scheduled posts at a time, and no LinkedIn first comment. If Buffer refuses, keep the rest for the next run.
- The @teedians.community account is a business account, so many trending songs aren't available until it switches to a creator account.
