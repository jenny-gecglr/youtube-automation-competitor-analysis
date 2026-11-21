---
name: youtube-automation-competitor-analysis
description: A complete workflow for building a faceless YouTube automation channel from the ground up, from competitor analysis and channel setup to an audited master prompt and the script of the first video. Analyzes a new YouTube competitor channel end to end (collects the data automatically, builds a channel identity card with a genre guess first, then niche, language gap, titles, thumbnails, scripts, reading level, CTAs and a comparison with your own channel), pulls the questions for a master prompt out of the competitor, then writes the master prompt and audits it in rounds. Use when someone says "analyze this competitor", "new channel analysis" or "prepare a master prompt from this competitor". It starts by asking whether you want a quick analysis (about 30-40 minutes) or a deep analysis.
---

# YouTube Automation Competitor Analysis and Master Prompt

It works in two modes, chosen first (see Step 0): **quick** and **deep**. The deep mode has two jobs: **(A) analyze a new channel, with the data collected automatically (the user never downloads anything by hand), and (B) turn the analysis into a master prompt and audit it.** There are no channel-specific examples baked in; every new channel is worked from scratch with this method.

In this skill, **the strong model** means the mid-to-high tier model that runs the main session (for example Sonnet 5.5). **The strongest model** means a tier above it and is used only with the user's explicit approval (see the model rule below). **Cheap tools** are Gemini, ChatGPT, NotebookLM summaries and, only when those are not enough, a small Claude model.

## Step 0: choose the mode (ask this FIRST, before anything else)
Before collecting any data or spending any credit, ask the user one question and wait for the answer:

> **Do you want a quick analysis or a deep analysis?**
> - **Quick** (about 30-40 minutes): the 15 most viewed videos, code measurements, ONE agent reading, a one-page yes/no form, and the approved rules written into the master.
> - **Deep** (the full workflow): the channel identity card first, then the data pack, titles, thumbnails (20 items), scripts, minute-by-minute video watching, reading level, CTAs, language gap, topic scoring and an audited master prompt.

- If the user chooses **quick**, follow the part called "Quick mode" below, then stop.
- If the user chooses **deep**, skip the quick part and start at the heading "Deep mode starts here" (part A comes right after it).
- If the user is not sure, recommend **quick**: it is cheap and shows whether a deeper look is worth it.
- The user can move from quick to deep at any time ("go deep", or the name of a deep step). The data pack that quick mode already collected is kept; deep mode starts with the channel identity card (A2) from that data, then adds only what it needs (for example the 3 least viewed videos).
- If the user's request already names the mode ("quick analysis of ...", "go deep on ..."), do not ask again. Either way, get the channel link and the language of the channel before the first step.
- Part B (turning an analysis into an audited master prompt) and the rule that the master is not written until the analysis is complete (B1) belong to the deep mode; quick mode has its own short master step.

## Setup check (first run)

After Step 0, before the first step of the chosen mode, check that every tool this skill needs is installed and signed in. For anything missing, say what it is and what it is for, then **ask before installing**. Never type or store passwords: sign-ins (Google, vidIQ, NexLev) are done by the user in the browser.

| Tool | Check | Install |
|---|---|---|
| Python 3 | `python --version` | Install from python.org |
| `yt-dlp` | `python -m yt_dlp --version` | `pip install yt-dlp` |
| Pillow | `python -c "import PIL"` | `pip install pillow` |
| Node.js | `node --version` | Needed by `yt-dlp --js-runtimes node`. Install from nodejs.org |
| NotebookLM CLI (`nlm`) | `nlm --version` | `uv tool install notebooklm-mcp-cli` (or `pipx install notebooklm-mcp-cli`) |
| NotebookLM sign-in | `nlm notebook list` | `nlm login`. The user signs in to Google in the browser |
| vidIQ MCP (outliers, VPH, keywords, channel search, video watching) | its tools are listed in the session | Add the vidIQ MCP server to Claude Code and sign in. Without it, the Outlier/VPH, keyword and language-scan steps cannot run; say so and ask the user for vidIQ screenshots instead |
| NexLev MCP (optional second source for outliers) | its tools are listed in the session | Add the NexLev MCP server and sign in. Optional |
| Second model CLI (optional) | for example `gemini --version` or `agy --version`, and `codex --version` for ChatGPT | Install and sign in. Without them, use a cheaper Claude model for the "cheap tool" jobs and keep the strong model for checks |
| ffmpeg (video splitting and sound measurement for A6b/A6c; also Whisper fallback transcripts) | `ffmpeg -version` | Install only when a step needs it (watching a local video, measuring sound, or a transcript that cannot be had any other way), and ask first |

If a required tool cannot be installed, stop and tell the user what is missing instead of continuing with a weaker substitute. Install only what the current step needs.

Two long-form references sit in `reference/`: `method-and-rules.md` (the philosophy, standard questions, the thumbnail detail list (A5 extends it), CTA rules, rule validation, common mistakes and the reason behind each rule) and `ready-made-prompts.md` (prompts for running the steps by hand). Read them when a rule needs its reason or a step needs more detail.

The seven helper scripts live in this skill's `scripts/` folder: `fetch_competitor_data.py` (data pack), `measure_channel_identity.py` (identity measurements from a transcript), `measure_genre_curve.py` (views-versus-age curve), `verify_punctuation_repair.py` (proves a punctuation repair changed no word), `measure_reading_level.py` (sentence ratios and readability on the punctuated text), `measure_title_duration.py` (quick mode: title patterns, durations and views) and `make_quick_form.py` (quick mode: the yes/no/note form). Run them with `python -I -X utf8`. In the commands below `<data folder>` is wherever you keep competitor data and `<competitor folder>` is `<data folder>/<channel name>/`.

## Principles (do not break)

1. **Format from the competitor, topic from you.** The formula that works is kept; topics and sentences come from your own niche.
2. **Adapt the mechanism, never copy the wording.** What works in the competitor is a **mechanism** (for example opening on an everyday moment and breaking it with "but think about this", a concrete promise of understanding, one carrier analogy, a short polite subscribe request at a natural point, a title that leaves a curiosity gap). It is adapted to your topic **in your own sentences**. The **wording itself** (sentence, scene, example, signature phrase, title, thumbnail image) is never taken. Write the mechanism into the master with a "why it works" reason (causality from a small sample is `[UNVERIFIED]`) and have each video build its own example in its section card. Following a format is a conscious decision and carries a **risk of resembling one competitor too closely**; state that risk openly in the master and offer a distinguishing signature element (palette, thumbnail, skeleton) as an option.
3. **No verbatim translation, ever** (sentence, skeleton, scene, signature phrase, character, proper name). A translation or summary made only for your own reading is fine. The competitor's visuals and video are never copied.
4. **With data and tools at hand, no guessing and no inventing.** Everything countable is counted with code; what cannot be fetched is written as "unavailable".
5. **The user does not hand over files.** We build the competitor's data pack ourselves (scripts, NotebookLM and its extension, Gemini, ChatGPT, other agents). The user provides only the channel link and the decisions. Fetch the number of items requested. If no script was requested, write none.
6. **Do not decide on your own.** Offer options, the user picks. Nothing enters the master without approval. **Titles, thumbnails and hooks belong to the user**; the agent never rewrites them.
7. **Say every foreign expression with a translation next to it** (when the user's language differs from the analyzed one). No long or medium dashes in the output.
8. **Do everything the cheap tools can do with them first; the strong model does the final check and writes the master.** The producer is not the checker: everything a cheap tool produces is checked by the strong model, and a pass mark comes only from code output or an independent checker, never from the author.
9. **Labels:** `[MEASURED]`, `[AI COMMENT]`, `[USER OBSERVATION]`, `[UNVERIFIED]`. Extra labels: `[OBSERVATION]` (a reading, no causality), `[COMPETITOR A6c]` / `[COMPETITOR A2d]` (seen in the competitor), `[COMPETITOR]` (seen in the competitor), `[USER <date>]` (the user's decision on that date), `[SUGGESTION]` and `[WRITER PROPOSAL]` (the user has not approved yet), `[OPEN]` (an open decision).
10. **Look before you search:** check the existing data pack in `<competitor folder>` and earlier decisions first, then run new searches.
11. **Do not scan before you know the channel (deep mode):** build the channel identity card first (A2). A cheap agent's classification or scan is always verified on samples by the strong model. If two different queries contradict each other, the result is written as "unreliable" and is not decision evidence.
12. **Quota or errors:** do not insist; tell the user.

---

## Agent work and the strong model's check (mandatory table)

**Rule:** every job done by a cheap tool (a small Claude model, Gemini, ChatGPT, a NotebookLM summary) is verified by **the strong model** with the minimum check below. The agent saying "I verified" does not count. **The result is written as a "Verification" section at the end of the analysis file** (what I checked, how many samples, result). If one sample is wrong, the whole job is **unreliable**: either raise the sample count and check again from the start, or have the job redone. Unverified lines carry `[UNVERIFIED]`.

**MODEL RULE (always, to save tokens):** the default order is: **big reading, listing, comparison and scanning jobs are done by Gemini (`agy`) or ChatGPT (`codex exec`)** (a small Claude model only when those are not enough or the job needs context; this keeps Claude tokens) → **a DIFFERENT tool, or a mid-level agent, checks it independently** → **the main session (the strong model) does the final check.** No unchecked job is accepted. **The strongest model is NOT sent without the user's approval**: ask every time, and an earlier approval does not carry over to the next time. It is used only if the user wants it and approves (for example, after everything is approved, the user says "check once more with the strongest model"). Writing the master or a script is the strong model's job, not the strongest model's. **Final check for the master:** after all other checks are done, the master is checked once by a strongest-model agent (independent, holistic reading, does not touch the file, report only); the user is asked every time and nothing is sent without approval. Lesson: a master draft was once given to a strongest-model agent without asking; the user accepted it that one time and said "ask next time", so always ask first.

**Two-tier check (saves tokens):**
1. **First check: a mid-level Gemini or ChatGPT agent (or code).** A **different** tool than the one that did the work checks it (if the small Claude model did it, Gemini or ChatGPT checks; if Gemini did it, ChatGPT checks and the other way round). Everything countable is checked with **code** (free). For the check prompt, give the agent only the raw data and "count/find it yourself" questions; do not show it the claim (so it does not just trust the claim).
2. **Final check: the strong model.** It does not read the raw outputs. It compares the **short report** of the first check against the code and the claim, re-looks at no more than 2 samples itself if needed, writes the "Verification" section and approves. If the first check and the claim disagree, the job is unreliable.
3. **Checks that need the vidIQ/NexLev MCP** (re-searching, re-measuring) do not work in Gemini/ChatGPT. A second independent small Claude agent or the user's own vidIQ screen does them, and the strong model reads only the difference.
4. **How to call them (tested):** ChatGPT: `codex exec --skip-git-repo-check - < prompt.txt` (give the prompt on stdin; do not pass a multi-line prompt as an argument). Gemini: `agy -p "$(cat prompt.txt)" --print-timeout 240s` (90 seconds was not enough for a 17-title job). Both counted the raw data themselves and reached the same result as the code (title-ratio test: identical to code). Personal information, employer names, finances and CVs are never given to these tools.
5. The final check's result is written in the analysis file's **"Verification"** section: who did the job, which tool did the first check, how the strong model did the final check, result.

| Job | Who does it | Minimum check (first check by a Gemini/ChatGPT mid-level agent or code; final check by the strong model) |
|---|---|---|
| Fetching transcripts (A2, A2b) | script + NotebookLM | Is each transcript's word count plausible (for example more than 1,500)? Do the first 20 words match the video's topic (by code)? The "unavailable" list is shown to the user |
| Channel identity card, genre (A2) | the strong model itself + code | If the reading and the code measurement conflict, the card says so; counter-evidence is written; the user approves |
| Popular-title scan by Outlier/VPH (B1b) | cheap agent (small Claude model) | Re-run at least 2 queries; open at least 3 of the 10 videos and compare title/views/VPH/Outlier; check the ranking is by Outlier and VPH, not by views |
| Language scan (A3b step 0) | cheap agent | Re-run the same query in at least 2 languages; if the counts do not match, the scan is "unreliable" and is not decision evidence; manually check at least 5 channels from the agent's classification (competitor / lesson / unrelated) |
| Translated keyword measurement (A3b step 2) | the strong model writes the translation, a cheap agent measures | Re-run at least 2 rows (one in a Latin script, one in a non-Latin script); rows under "<750/0" are marked "no data", not used as a reason to eliminate |
| Translated-title test (A3b step 3) | cheap agent | Re-run at least 1 query and compare the "target format" count; note borderline cases (sleep documentary, face-on-camera host, lesson) |
| Title analysis (A4) | ratios by code; translation and overlap search by a cheap agent | Recompute the ratios with code; re-search at least 5 of the titles that were declared "no overlap" on YouTube; character limit by code |
| Thumbnail analysis (A5) | Gemini (`agy`), spot-checked by a small Claude model | Open at least 4 thumbnails visually and compare with the rows (the 2 most viewed, 1 least viewed, 1 exception; the A5 verification paragraph raises this to at least 8); the strong model recomputes the counts and checks the date order against the metadata; redo the HAND TEST on at least 2 thumbnails; check at least 3 rows of the title-thumbnail text mapping table against the real thumbnails; recount shared-pattern counts (for example "red underline 5/17") from the rows |
| Script analysis, summary, lesson/rule extraction (A6) | NotebookLM / cheap agent | Search at least 5 of the summary points in the transcript (quote and position); recompute numeric claims with code; if anything is invented, the whole summary is unreliable |
| In-video visual and audio analysis (A6b) | Gemini (`agy`) on a local file with splitting (recommended); vidIQ `vidiq_video_watch` only as a backup | Compare numeric claims (cut rate, visual share) with at least 2 frames or a short clip; the "is the voice AI" verdict is `[UNVERIFIED]`; look for contradictions with the transcript, since a speech summary is not requested |
| Punctuation repair (A7) | cheap agent | **The word sequence must be compared word for word by code (mandatory)**; if it differs, have it fixed; sentence ratios are labeled "approximate" |
| Code measurements (CTA, markers, curve) | Python | Find at least 1 CTA position in a transcript by hand and compare it with the percentage |
| Rules list, filling the question form from the competitor (A11, B2) | cheap agent drafts | Every "In the competitor (measured)" cell is checked against the number in the analysis file; a cell without a source is left empty |
| Scoring topics and competitor videos (B1b 3b) | cheap agent (small Claude model), with the vidIQ MCP | Re-run at least 2 topics and compare the Outlier/VPH values in the table; re-fetch at least 3 videos from the competitor's popular list with `vidiq_channel_videos`; check that the sort is by Outlier/VPH and that excluded video types are marked in the list. If there is no agent, the strong model cross-checks the data with a second measurement |
| Channel name suggestions (A10) | Gemini writes; an MCP-enabled cheap agent checks overlaps | Search at least 5 of the suggestions in `vidiq_youtube_search` channel mode (needs the MCP, so Gemini cannot); a second independent agent or the strong model re-searches; check the translations and that the main keyword appears |
| Channel description (A10) | the strong model writes | Code: 1000-character limit, chosen keywords present, no warning or legal paragraph |
| Logo/banner prompts (A10) | Gemini | By code and eye: the competitor's logo was downloaded (file exists, square), every prompt repeats the common style block word for word, "no text" and the 1546x423 safe-area wording are present, the competitor's main color tone is not used; the user picks among the generated images |
| SEO keyword list (A3b step 5) | vidIQ screen (user) + MCP | Compare at least 2 of the MCP values with the user's screenshot; the user's screen is authoritative |
| Script, master (B) | the strong model writes (a strongest-model agent ONLY if the user approves) | A separate zero-context strong-model checker + code + final judge (B3, B6); the final scan of the master against the competitor analysis is A13 (Gemini/ChatGPT lists, a mid-level agent checks, the main session does the last check) |

---

# Quick mode (about 30-40 minutes)

Use this part when the user chose **quick** in Step 0. It pulls the 15 most viewed videos of the competitor, measures them with code, has ONE agent read them, gives the user a one-page yes/no form, and writes the approved decisions into the master. Target: 30-40 minutes. If the user later says "deep" (or asks for one of the deep modules below by name), keep the data already collected and go to the matching step of the deep mode (the A and B sections after this part); do not copy it, jump to the step number. There are only two modes, so the scope does not grow.

## Rules
- The small tool does the work (code, Gemini `agy`, ChatGPT `codex exec`), a medium agent or a different tool checks it, and the main session makes the final check. **The strongest model is used only if the user asks, asking each time.**
- Quick mode spends no credits (it uses only free tools). Credits (vidIQ MCP, NexLev, Flow) belong to the deep mode, where you state the cost and ask the user before any bulk spend (language scan, video watching, name checks, image generation); use the free route first.
- No sentence, signature phrase, scene or thumbnail image is copied from the competitor; the **mechanism** is taken. Titles, thumbnails and hooks belong to the user; the agent does not rewrite them.
- No employer names anywhere. Personal information is not given to outside tools.
- Gemini runs at most 2 jobs in parallel, 20-30 seconds apart; if it returns empty, switch to ChatGPT.
- For searching, use plain `grep -n -i "word" file`. Do not fall into the `grep -o '.{60}x.{60}'` trap.
- Never write "verified" for something that was not measured; write only what was measured. No long or medium dashes (scan with Python). Put a translation next to every foreign expression.
- Labels: `[MEASURED]` (code), `[OBSERVATION]` (agent reading, no causal claim), `[AI COMMENT]`.

## Steps

### 1. Fetch the data (5-10 min, code, no tokens spent)
```bash
python -I -X utf8 scripts/fetch_competitor_data.py <channel-url> <data folder>/<channel> --count 15 --least 0 --lang <en|de> --name "<channel name>"
```
Output: `titles.txt`, and in each folder under `videos/`: `meta.json`, `title.txt`, `transcript.txt`, `thumbnail.jpg`; also `thumbnail_measurements.json` and `_summary.md` (with the UNAVAILABLE list). The script takes the transcript from NotebookLM. If it is missing, try in this order: the NotebookLM extension, Whisper, then write "unavailable". Date, views and duration are in `meta.json`; look there before writing "unknown". Quick mode uses only the 15 most viewed videos (`--least 0`); if you go deep, the 3 least viewed are added then (and check their real views in `meta.json`, because the script takes them from the channel's listed page).

### 2. Measure with code (5 min, `[MEASURED]`)
- Channel identity and CTA positions: `python -I -X utf8 scripts/measure_channel_identity.py <transcript.txt> <output.json>` (run it on the most viewed video's transcript, and on the others in a loop if time allows) (the CTA count can be wrong; confirm the percentages in the transcript with `grep -n -i`).
- Genre curve: `python -I -X utf8 scripts/measure_genre_curve.py <data folder>/<channel> <output.json>`
- Title patterns (digits, "you" address, question marks, word count, character count, separators, "how to"), the most common first words and word pairs, and the duration and views distribution: `python -I -X utf8 scripts/measure_title_duration.py <data folder>/<channel> <data folder>/<channel>/title-duration-measurements.json` (about 4 seconds on a 343-title channel).
- Language level: transcripts are mostly **unpunctuated**, so sentence length and Flesch cannot be measured from this text. Use proxy measures that need no punctuation: word count, unique-word ratio, the most repeated words, average word length. Write the level (B1/B2/C1) as a **comment**, `[AI COMMENT]`. If sentence measurement is needed, use the deep module.

### 3. ONE agent reading (10 min)
Gemini: `agy -p "$(cat prompt.txt)" --print-timeout 240s`, or ChatGPT: `codex exec --skip-git-repo-check - < prompt.txt` (give the prompt on stdin). Give the agent the raw data plus the step 2 measurements and ask for:
1. Common and different features (title, opening, structure, CTA positions, language).
2. "Why it worked": **only `[OBSERVATION]`**, no causal claim, with a survivorship-bias note (we only see what worked, we do not know what did not).
3. **15 rule candidates**, each with: the mechanism, the video where it was seen in the competitor, and the risk (closeness to copying).

Output: `<competitor folder>/quick-reading.md`. If the agent writes new example sentences, run a 5-word closeness scan against the competitor (code: any 5 consecutive words that match).

### 4. One page and a form for the user (5 min)
Ready tool: write the agent's 15 rule candidates as an `items` list in JSON (`{title, summary[], items[{id, title, description, suggestion}]}`), then run `python -I -X utf8 scripts/make_quick_form.py input.json <competitor folder>/quick-form.html`, and publish the resulting file as a shareable page. The form has a summary on top, **Yes / No / Note** for every rule, and **"Copy result"** at the bottom; the user pastes the text into the chat. Skeleton if the tool is not available:
```
<h1>Channel name: quick analysis</h1> <section id=summary>10-line summary</section>
<ol id=rules> <li data-id=R1>rule, mechanism, video
  <label><input type=radio name=R1 value=yes>Yes</label> <label>...No</label>
  <input type=text placeholder=note></li> ... </ol>
<button onclick=copyResult()>Copy result</button>
// copied text: 1) rule title: Yes | NOTE: ...  (one line per rule, like the real tool)
```
Save what the user pastes as `<competitor folder>/decisions.md`. Nothing is written into the master until the decisions arrive.

### 5. Write into the master (5-10 min, the strong model writes)
Template order: the channel's latest master; if there is none, the B3 structure of this skill (workflow, hook approval, quality loop, CTA section). Only the rules the user said "yes" to are added, with the "why it works" reasoning and the `[OBSERVATION]` label; rules with notes follow the user's note. The version number is raised and the old master is backed up, never overwritten.

### 6. Check (5 min, no extra round)
- **ONE independent check:** a DIFFERENT tool from the one that did step 3 (if Gemini did it, ChatGPT checks, and the other way round). Questions: does every rule written into the master match a "yes" from the user, did any "no" leak in, is there a sentence or signature copied from the competitor.
- Write the check result to `<competitor folder>/check-report.md`.
- **Final check in the main session:** a dash scan by code, an employer-name scan, the 5-word closeness scan, and a re-look at 2 samples from the check report.
- Non-critical findings go to a "Later" list (`later.md`) and do not open a new round. Only critical ones are fixed (copying, an employer name, a user "no" leaking in).

## Switching to deep mode (only when the user says "deep"; the modules link to the deep sections)
| Module | Where |
|---|---|
| Video watching (Gemini, in pieces) | sections A6b, A6c |
| Detailed thumbnail analysis | section A5 |
| Foreign-language and old-master comparison | sections A3b, A9 |
| Punctuated reading level, sentence measurement | section A7; `scripts/verify_punctuation_repair.py`, `scripts/measure_reading_level.py` |
| Keyword volume (Google Trends + the vidIQ web screen, no credits) | section B1c |
| Channel setup (name, description, logo) | sections A10, A10b |
| Final scan of the master against the analysis | section A13 |

## Output files (`<competitor folder>/`)
`titles.txt`, `_summary.md`, `thumbnail_measurements.json`, `channel-identity-measurements.json`, `genre-curve-measurements.json`, `title-duration-measurements.json`, `quick-reading.md`, `quick-form.html`, `decisions.md` (what the user pasted), `later.md`, `check-report.md`.

# Deep mode starts here
Everything from here to the end (parts A and B and the report) is the deep mode.

# A. Analyze the new channel

## A1. Clarify the input
Channel link(s), target language, scope. The user does not provide files; we build the data pack (A2b). Ask few questions, and make them multiple choice.

## A1b. Candidate competitor list: a ranked table, the user chooses (BEFORE the analysis)
When there is more than one candidate channel (for example from the language scan or from the user's own list), first produce the table below. **The user looks at the channels with their own eyes and chooses**; a channel they did not choose is not analyzed.
- For each channel: **channel name (a clickable YouTube link), subscribers, total views, video count**, ranked by total views (most to least; rank by subscribers separately if needed). Gemini, NotebookLM or a small Claude model collects them, and the numbers are **verified a second time by code** (yt-dlp, the channel's /about page); vidIQ is not used.
- **Check language and topic fit first:** the list can contain a channel in the wrong language or off topic (for example a Spanish channel had entered an English list); write a warning note for the user. Note whether the channel is purely on the topic or mixed (for example it also covers other subjects).
- If several channels share the same name (for example small channels with the same name), pick the right one with a sample video ID; a channel that cannot be found or was deleted is **skipped, never guessed**.
- Write the user's choice to a decision page (chosen, not chosen, and why).

## A2. Know the channel FIRST: the most viewed video's transcript, a reading, a code measurement, the channel identity card
**Why:** a scan made without understanding the channel brings the wrong competitors (in a trial on a physics explainer channel it was taken for a lesson channel, and school and exam channels were counted as competitors). The language scan, competitor search, thumbnail/title comparison and the data pack **do not start without this step and the user's approval.**
1. **Have NotebookLM fetch the transcript** (the model spends no tokens): only the **most viewed video** (the 3 most viewed if needed):
```bash
python -I -X utf8 scripts/fetch_competitor_data.py <channel-url> <data folder>/<channel name> --count 1 --least 0 --lang <language code> --name "<competitor channel name>"
```
The script opens a **persistent** NotebookLM notebook named after the competitor, adds the video and writes the verbatim text with `nlm source content`. Later runs reuse the same notebook; a video already there is not added again.
2. **The strong model reads** the transcript from start to end (the real text, not a summary; for evidence, quotes under 15 words with a position %).
3. **Check with Python code (the strong model runs it and interprets):**
```bash
python -I -X utf8 scripts/measure_channel_identity.py <transcript.txt> <competitor folder>/channel-identity-measurements.json
```
It measures: word count, unique-word ratio, pronoun density (you/we/I), marker densities (lesson/exam, story/history, analogy, curiosity question, honest caveat, sensational words), CTA positions (%), references to earlier videos, a hook sample, and rhythm over 10 slices. It needs no punctuation. If the reading and the measurement conflict, the conflict is written on the card.
4. **Write the card** (`<competitor folder>/channel-identity.md`): a **one-sentence result** (lesson? popular-science narrator? documentary? news? vlog? story?...) plus evidence: hook and promise, structure (the story arc section by section), narration style, language level and target audience, depth of knowledge, CTA (percentages measured by code), series links, visual style (from the thumbnail), voice (human/AI `[UNVERIFIED]`), the gap between title packaging and body, and the **genre guess** (see below).
5. **Write the competitor definition:** who counts as a competitor, who does not, who partly (lesson/exam/academic channels count only if the channel really is a lesson channel), plus the **scan query and the exclusion list**.
6. Show the user the short card: "is the channel this?" After approval go to A2b. If they correct it, update the card.

### Genre guess (part of the card, mandatory)
The channel's genre (**Evergreen, Cashcow, Trend, Hype**; it can be mixed, for example "80% cashcow, 20% trend") is written on the card as a **first guess**, because later analysis changes with the genre (keyword weight, formula, speed, thresholds, decision time). Standard definitions: **Evergreen** is timeless search/recommendation content watched for years (education, guides, timeless documentaries; critical factor: the first 5 seconds of the opening and the exit in the last 5-10 seconds); **Cashcow** is a repeatable-formula niche revenue channel, automated or semi-automated (for example a channel about life on a ship; critical factor: a curiosity-raising thumbnail and the first 30 seconds); **Trend** is current, seasonal search volume that must be caught fast (news, game and technology updates; critical factor: speed, caught within the first 24 hours); **Hype** is an instant viral burst (challenges, viral clips; critical factor: click and curiosity). Mixed genres exist, for example "trend cashcow". Evidence:
- **Topic timelessness:** currentness markers (this week, breaking, year) and timeless markers in the most viewed video (output of `measure_channel_identity.py`).
- **Formula repetition:** does the same title pattern and video skeleton repeat (a cashcow sign)?
- **Packaging:** keyword/question titles (evergreen), shock/curiosity titles (cashcow/hype), dates and current names (trend).
- **Production speed and view curve (after A2b, by code):** `python -I -X utf8 scripts/measure_genre_curve.py <competitor folder> <competitor folder>/genre-curve-measurements.json` gives upload frequency, daily views by age (videos older than 7 days), the newer-to-older half ratio, and the **single-video share** (more than half = a single hit, not a true evergreen/cashcow).
- Write a confidence level (low/medium/high) and the **counter-evidence**. For a very young channel (about 40 days) confidence is low; CTR, average view duration and the first 30 seconds cannot be seen on a competitor (only the owner has them).

| Signal | Evergreen | Cashcow | Trend | Hype |
|---|---|---|---|---|
| Topic timelessness | high timeless, no currentness | timeless or niche-bound | high currentness | current / event-driven |
| Formula repetition | pattern not required | **strong formula**, same skeleton repeated | varies by topic | one-off spectacle |
| Packaging | keyword, question | curiosity/shock wording + parentheses | date, current name | extreme claim, challenge |
| Production speed | low to medium | high (automation) | very high, fast | variable |
| View curve | old videos still watched | slow, steady growth | heavy in the first days, then drops | one burst, then fades |
| Top video share | low | low | medium | **high (over half = single hit)** |
| Niche | constant search volume | revenue (RPM) driven niche | news/games | viral |

| What changes by genre | Evergreen | Cashcow | Trend | Hype |
|---|---|---|---|---|
| Look first at | keywords, search volume, timeless topic list | **formula**: title pattern, structure, thumbnail family, production speed | topic speed, first 24 hours, the competitor's reaction time | viral trigger, single-hit threshold |
| Language choice | **keyword volume** (Monthly searches) decides | gap + how cloneable the formula is | the language with a news flow | a large market |
| Title/thumbnail | keyword + curiosity | curiosity/shock + parentheses | date + current name | extreme claim |
| Master priority | first 5 seconds of the opening, exit in the last 5-10 seconds, depth | first-30-seconds hook, formula consistency | speed, short production chain | click focus |
| Thresholds for your own channel (CTR / average view percentage / first 30 seconds retention) | CTR 5-7%, 35%+, 75%+ | CTR 8-10%, 30%+, 65-70% | CTR 10-12%, 30-35%, 70-75% | CTR 15%+, 25-30%, 70%+ |
| Decision time (when to judge whether to continue) | 31st video | 31st video | 15th video | a few days |

If the user has their own genre rule, use that instead. The counts above are rough markers, not verdicts `[UNVERIFIED]`. **The user approves the genre** (it is added to the card). The genre sets the language-choice criterion in A3b and the master's priorities: in Evergreen keyword volume decides, in Cashcow formula and gap, in Trend speed.

## A2b. Collect the data pack (after the card is approved; the user downloads nothing by hand)
For the competitor's **15 most viewed + 3 least viewed videos** (the video fetched in A2 is not fetched again; the same folder and notebook are used), everything by script, without spending the model's tokens:

```bash
python -I -X utf8 scripts/fetch_competitor_data.py <channel-url> <data folder>/<channel name> --count 15 --least 3 --lang <language code> --name "<competitor channel name>"
```

**The transcript comes from NotebookLM** (no tokens): the script adds the videos to a **persistent** NotebookLM notebook named after the competitor and writes the **verbatim** text with `nlm source content` (no model in between). The notebook is never deleted; its id goes in `_notebook.json`; the same notebook is used if the same competitor is run again. If NotebookLM cannot deliver, the yt-dlp subtitle is tried.

The script (yt-dlp + Pillow) writes all of the following under `<competitor folder>/`:
- `titles.txt`: all titles, most viewed first, with exact views.
- In each video folder: `meta.json` (exact views, date, duration, likes), `title.txt`, `description.txt`, `description_links.txt`, `chapters.txt` (the 0:00 lines in the description), **`transcript.txt`** (verbatim from NotebookLM, or from recorded/automatic subtitles as a fallback; raw, never translated or changed), **`thumbnail.jpg`** (maxres, hq if missing).
- `thumbnail_measurements.json`: size/ratio, brightness, saturation, dominant colors and top-strip color for each thumbnail `[MEASURED]`.
- `_summary.md`: a table + the **UNAVAILABLE** list.

**Transcripts come only from NotebookLM and its extension; no vidIQ or NexLev credits are spent on transcripts.** If the script fails or a transcript is missing, in order:
1. Add the video to the notebook with the NotebookLM extension (Chrome) and take the text.
2. Extract it from the audio with Whisper (ffmpeg + Whisper installed; ask the user first).
3. If it is still missing, write "unavailable" and show it to the user in the list. Never invent a summary.

**VPH and Outlier:** the script gives views; get VPH and Outlier scores with NexLev (`youtube_channel_outliers`) and vidIQ (`vidiq_outliers`) and write them **side by side** (the two scores are computed differently). If a video with a high Outlier is not among the 15, add it to the list. Whether Shorts are in or out is the user's decision.

**Multi-competitor analysis:** the user prepares no files; agents collect the competitors' high-Outlier videos themselves with NexLev/vidIQ (only for Outlier/VPH) and NotebookLM into one data file, then analyze the file in detail, listing links and titles. Ranking is by Outlier + VPH together. Output table: rank, Outlier, VPH, views, channel, original title, target-language title, **what it really says (nothing invented)**, keywords.

## A2c. Saving tokens: who does what (ChatGPT, Gemini, NotebookLM)
Heavy and raw jobs go to the cheap tools; the strong model's tokens are for writing, checking and deciding:

| Job | Tool |
|---|---|
| Collecting data (list, description, thumbnail, measurements) | Script (yt-dlp + Pillow), nobody reads it |
| Verbatim transcript, video summary, rule/lesson extraction | **NotebookLM** (a persistent notebook per competitor, queries tied to sources) |
| Simple/judgment work: reading thumbnails, first draft analysis, link/source scanning | **Gemini** (`agy -p`, output to a file, the strong model reads only the file) |
| First drafts, second opinion, bulk classification | **ChatGPT** (Codex) |
| Language level / sentence ratio / counting | Python |

**Limits (fixed):**
- **Scripts (the video text), the master and the Python checker scripts are always written by the strong model.** ChatGPT, Gemini and NotebookLM never write a script or a master.
- **All checks (checker, final judge) are done by the strong model.** Everything the other tools produce is checked by it; unchecked work does not pass.
- No personal information, employer name, finances or CV goes to ChatGPT/Gemini/NotebookLM.
- A NotebookLM answer is not verbatim; label it "NotebookLM summary". Only the `source content` output is verbatim.
- If the quota runs out, do not insist; tell the user.

**Division of labor:** collecting = script · measuring = Python · reading/summary/thumbnail description and every other doable job = Gemini / NotebookLM / ChatGPT first (all checked by the strong model, with the minimum check in the table above) · interpretation, writing and decision suggestions = the strong model.

## A2d. Common and different features across several channels, and "why did they work" (after the identity cards)
When several competitors are analyzed, after each channel's identity card list separately the **common features, the different features and the outliers (what only 1-2 channels do)**; do the same for thumbnails (see A5c). **The order is mandatory:** (1) **a small agent lists** (a channel x feature table, including conflicts between a card and the measurements); (2) **a mid-level agent verifies the list against the cards** (it recounts at least 6 claims by code or from the transcript) and works the question "why did they work": verified common mechanisms, real differences, the small agent's mistakes, **mechanisms (not wording)** that could be adapted to our channel, risks, what the sample cannot say, and questions for the user; (3) **the main session** recomputes the numbers by code, does the final check and presents it to the user. The aim is to understand why channels with millions of views worked and to build ours accordingly. If the cards rest on a single video each, the results are a "first sign" (no causality, survivorship bias); they firm up when the 15+3 videos arrive from A2b. This step is done even with one video per channel.

## A2e. Measurement traps and known tool errors (watch for these while writing the card)
- `measure_channel_identity.py` was seen **making mistakes in CTA counting** (in an independent check of 7 cards): it can miss "like" and "share" calls, count the same "comment/subscribe" sentence twice, take a phrase such as "feel like" for a like CTA, and not count years such as "1980s". When writing the card, **confirm the CTA percentages by searching the transcript** (word position / text length); when the card and the JSON disagree, write the conflict. Fixing the tool is a separate job.
- **Before writing "date / views / duration unknown", look at `meta.json`:** views, date, duration, likes and comment count are there; a card once wrongly ignored them.
- **Blank views in a channel listing** (hundreds of videos showing 0 or blank in the `yt-dlp` channel listing) can be a listing error, not corrupt data; take views from each video's own page. Write the difference between the channel total and the sum of the listed videos; do not guess.
- **Verifying a suspicious channel:** check the like ratio, views per subscriber and the consistency of totals (for example a like ratio of 0.47% while the channel median is 2.19%); a low like ratio alone is not proof of fake views. If it cannot be measured, write "CANNOT TELL" and the user decides.
- **Sample reminder:** a card that rests on a single video is a "first sign"; "why it works" sentences are hypotheses.

## A3. Three-layer ranking and channel assessment
Show separately in the output: **your own analysis, then NexLev, then vidIQ.** Write what each tool returned; a tool that returned nothing or ran out of credits is **stated openly**.
- **Genre:** the guess from A2 is confirmed with A2b data (`measure_genre_curve.py`) and the user approves. Niche detail, how it is made, positives/negatives.
- Can it be automated, how hard is the script to write, an easy production flow, which AI tools and editing method, how much cost and time.
- Can the same style be done with another topic?
- Growth speed, few videos and many subscribers, upload frequency, audience (age/gender/country), RPM.
- **Dependence on a single video** (more than half of the total) = not a true cashcow. **Clone network** = a sold template, saturation.
- **Study the worst videos** and a similar channel that did not take off.
- **Legal and policy risk** (copyright, "fake AI content", target-country rules): "what must I not do?"
- **Language gap:** list the competitors in the target language with links, search with four different keywords; a "no competitor" claim is verified with a current search and dated.

## A3b. Language and niche decision (before opening the channel, mandatory)
In order:
0. **Language gap scan (first, automatic; the user does not supply candidate languages).** The user cannot choose a language without seeing the analysis, so the **scan** produces the candidate languages. With vidIQ `vidiq_channel_search` (`query`: the competitor's niche summarized in English, `languages`: [language], `exactLanguage: true`, `channelType: long`, `limit: 10`; 5 credits per call) scan the default language list: de, fr, es, pt, it, tr, ru, pl, ja, ko, hi, ar, id, nl (it can change by channel type). For each language: how many channels come back, how many uploaded a video in the last 60 days, the strongest active channels (subscribers, 30-day views), the number of breakout (rising) channels, **clone signs** (channels copying the same format, for example the same figure's name in the channel name), and whether only school/exam/academic channels exist or a strong popular narrator exists. **Limit (trial on a physics explainer channel): this channel scan is a ROUGH first elimination, not decision evidence.** Semantic search also returns school/exam/academic channels; the `faceless: true` filter removes real competitors whose `isFaceless` is empty and brings unrelated channels (story, trivia, motivation); the channel classification (competitor/lesson/unrelated) is a cheap agent's opinion. Two different queries gave conflicting results for the same language. So **the real language test is the translated-title test (step 3)**: searching the competitor's translated titles on YouTube. The scan only narrows which languages enter that test. Genre detection (A3) is done **before** the scan; the query is built from the competitor's genre, and lesson/exam/academic channels do not count as competitors. **The raw output is very long (about 10-12 thousand words per call): the cheap agent (sub-agent/Gemini) runs the scan and returns only a short language table; the strong model verifies it with samples.** The table is shown to the user; the 3-4 languages with a visible gap become **candidates**.
1. **Keyword search in the competitor's own language (vidIQ).** Give the competitor's main keywords and the important word patterns in its titles to vidIQ in the competitor's language. For each keyword record: **Monthly searches** (very low/none = no interest) and, if shown on the screen, **hourly views**, the **competition color** (vidIQ's label: **Low = green, Medium = yellow, High = red**) and the **Keyword Score**.
2. **Translate and measure in the candidate languages (from step 0).** Translate these words and patterns into the candidate languages (Gemini/a cheap agent translates, the strong model checks; not a plain translation, but the term really searched in that language). In vidIQ, with that language and country setting, take the same measurements (Monthly searches, competition color, Keyword Score) and put the tables side by side. Very high competition can be a reason to give up.
3. **Translated-title test (in the candidate languages, mandatory before the decision).** In a language with a visible gap, **translate the competitor's 3 most viewed titles into that language and search YouTube**; see whether other competitors appear with the same or a similar title. The translation and search are done by Gemini/a cheap agent (with the vidIQ `vidiq_youtube_search` and NexLev `youtube_search` MCP tools) and the strong model checks. Record the result with a date.
4. **Language decision:** a yes/no suggestion with the table of steps 1-3 (measurements + competitor count/views). The decision is the user's. **If the user already chose the language (for example they open the channel in the competitor's own language, English), steps 0-3 are for information, not for the decision; the language choice stays theirs and you go to step 5.**
5. **After the language is chosen, a detailed keyword search in the chosen language.** Keywords, Keyword Score, competition color, important title patterns and analysis results are saved to `<competitor folder>/vidiq-keywords.md` and **go into the master's SEO section** (B7).
- Route: **vidIQ's own keyword screen is enough**: the Low green / Medium yellow (High red) label, Keyword Score and hourly views are read from that screen. You prepare the keyword list (translated into the candidate languages); the user pastes it into vidIQ and looks at the screen, and gives the values or a **screenshot**; you write them into the table (reading the screenshot with Gemini/Claude). If wanted, the `vidiq_keyword_research` MCP helps (tested: it gives volume 0-100, competition 0-100, an overall score, monthly searches and growth by country; it gives no color and no hourly views, so it does not replace the screen).

## A4. Title analysis
1. All titles from most to least viewed → repeated words → **formula**.
2. Translate into your niche, **keep the format identical**, with a translation next to it. Never rewrite the user's own titles; resemblance to the competitor is only an information note.
3. Every title is searched on YouTube; **no overlap**. Limit **100 characters**.
4. Variety: never start consecutive titles with the same word/letter. Look at the competitor's title history.
5. Ratios **by code**: command/prohibition ratio, "you" address, titles with numbers, word count, tone (command/statement/identity). The user's decision outranks the measurement.

## A5. Thumbnail analysis (20 items, mandatory in every analysis)
**Scope rule:** the thumbnail analysis is done with the thumbnails of the competitor(s) being analyzed. With a **single competitor**, use that competitor's thumbnails (from its own video data pack); with **several competitors**, use all of theirs; no separate "competitor for thumbnails" is searched for.
All `thumbnail.jpg` files are inspected by Gemini (`agy`) by really looking at them, in great detail (local files, `--add-dir`; use the A6b method: split into batches and run at most 2 jobs in parallel); a small Claude model spot-checks and the strong model gives the final check; numeric items come from `thumbnail_measurements.json`. The output is a **report**, and producing our own thumbnails starts from this report (A5b). One row per thumbnail:
1 format/ratio/strip · 2 composition · 3 fullness and balance · 4 color palette, tone, contrast, red accent, light · 5 figure, expression, pose, camera angle · 6 visual style and how it changed over time · 7 text (word count, line layout, typeface, color, **red word**, position) · 8 text content and translation, tone, "you" address · 9 extra elements (arrow, circle, logo) · 10 title + thumbnail + hook fit · 11 the emotion triggered ("what should they get?") · 12 consistency within the channel · 13 good and bad performers side by side · 14 **production recipe** (for a text-free image an English prompt + an explanation in the user's language; the text is added in Canva) · 15 measured / interpretation labeled separately.
16 **HAND TEST:** with the text covered by hand, does the picture alone tell the topic (PASS / WEAK / STAYS) · 17 **TEXT TEST:** does the text alone carry the idea; does the thumbnail text repeat the title, shorten it or add curiosity; does the thumbnail say what is inside the video.
18 **MEASURABLE FIELDS (a table, one row per thumbnail, everything an estimate with a plus/minus, UNSURE when not sure):** text area % · text height % · text line and word count, the words · text position (top, bottom, left, right, center) and alignment, which side of the picture the text is on · typeface class (serif, sans, slab, script, condensed), weight, all caps or not, type feel · text colors (approximate hex), accent word and its effect (outline, shadow, glow, underline color, box, arrow) · picture area %, where the main visual sits · main subject type and number of main objects · is there a person (none, silhouette, hand), is the face visible · background type and color · dominant 3 colors (hex and %) · text/background contrast · light and effects (glow, rays, particles, vignette, blur) · extra marks (arrow, circle, question mark, number, badge) · emotional trigger.
19 **STYLE REPETITION (chronological, by thumbnail dates):** group the thumbnails into TEMPLATES (same layout, typeface and color logic); the sequence of templates by date and **how many videos the same style lasts before it changes (average run length)**; which elements are always fixed (typeface, text position, accent) and which change; whether there is drift over time; the relation between template and views (template or topic: separate the pattern from the guess). Dates are in each video folder's `meta.json` (`date`).
20 **TITLE-THUMBNAIL TEXT MAPPING TABLE (mandatory):** one row per competitor video: title | the exact text on the thumbnail | relation type (a shortened title, the same question, the half of the title that makes you curious, a single emotion word, a number/claim, a new clue not in the title) | word count | accent word (does it come from the title) | how many title words repeat on the thumbnail. Then the table yields **"formulas for deriving thumbnail text from a title"** (for example "the title's striking word + a question mark"). For the title we pick, we derive 3-5 thumbnail text candidates with these formulas (the user chooses); the competitor's text is not copied, only the formula is taken. The thumbnail picture is produced WITHOUT text and the text is added afterwards (by the user in Canva, or by ChatGPT in the same conversation as in A5b step 5b), because text in AI images often comes out broken.
From the output, **measurable design rules** (ranges, for example "text area 15-25%") and a numeric description of the 5 most viewed and 5 least viewed are extracted; with a small sample they are written with an "inference" label.
At the end, a "shared pattern" and "exceptions"; also a **comparison of the 5 most viewed with the 5 least viewed** (separate the pattern from the guess, no causality from a small sample), **the relation between passing the HAND TEST and views**, the weak sides of the competitor's thumbnails and a list of **"10 principles of a good thumbnail"** (as principles, not copied visually). **How closely to resemble the competitor is not a general rule**; the user decides in each concept.

**A5 verification (mandatory, learned in the first run):** Gemini reads thumbnails well but makes mistakes in counting, dates and ordering. (1) A small Claude model compares at least 8 thumbnails with the real images (text, position, underline/arrow, background, main subject; in the first run 8 of 8 were correct); (2) the strong model recomputes the numbers from the table and compares the date order with the metadata (in the first run Gemini's story "video 01 blew up, then the clock thumbnails came" did not match the dates, it ordered the bottom 5 wrongly and miscalculated a median); (3) "rule" language is too strong for a small sample: findings are written as **observations**, each with a support level (WELL SUPPORTED / WEAK / CONTRADICTED); (4) hex color codes and color percentages cannot be verified by eye and are not turned into rules. Gemini is given the video upload dates (`meta.json` `date`) so it does not invent a date story.

## A5b. Producing our own thumbnails from the competitor thumbnail report (done while the video uploads)
A thumbnail is a layered, hard job: the competitor thumbnail report + our differences (brand style, mascot if the channel has one, honest facts) + **CTR** + **fit with the title** + **the real content of the video**. All of it is considered together. The order:
1. **The report must exist** (A5). If not, do it first; no thumbnail is produced independently of the competitor analysis.
2. **Gemini designs and writes the prompts** (the strong model's own prompts alone are not enough; a first attempt produced a meaningless concept). Gemini is given: the channel identity (style, palette, mascot, reference images), the approved title of the video, the hook and script, the honest message of the video, the competitor thumbnail report, the user's feedback, the HAND TEST requirement and a rule against misleading the viewer. Gemini designs at least 6 different concepts; for each: what is understood at a glance (the HAND TEST answer), click curiosity, a text suggestion (1-4 words, a single accent word), background, which references to attach, a complete ready prompt for ChatGPT, the risk of misleading; a ranking at the end.
3. **The strong model checks** (title, thumbnail and hook fit; misleading; palette/style).
4. **Every prompt is given to ChatGPT, every time, with:** the fact that this is a YouTube thumbnail and CTR-focused, the video topic and a description of a good thumbnail; the style reference image and style block; the mascot reference images if there is a mascot. All six are produced **in the same ChatGPT conversation** so the user can see them. (Whether ChatGPT produces images through its API is checked separately; for now through Chrome.)
5. **No decision without the user seeing it:** every image is shown to the user, the **HAND TEST is done together with the user**, and the ok/no comes from the user. No production without approval.
5b. **The thumbnail text can also be written by ChatGPT (varies by channel):** once the text-free image is approved, the text is written in the same ChatGPT conversation together with the image (the exact text, type style, text height about 11-15%, a top band, the accent underline color, with the instruction "keep the image exactly as it is"). On some channels the arrangement is different: ChatGPT makes only the IMAGE and the user adds the text by hand afterwards in Canva; then ChatGPT does not write the text and no text is overlaid by code. Adding text with the agent's own code is not part of the method.

6. The report and results are written to the notes (the raw report and the compiled findings).

## A5c. Main result of the thumbnail analysis: 7 main art-style clusters (the detail is a separate optional step)
Gemini reads the thumbnails in detail (A5; one competitor's thumbnails, or all of them when there are several competitors). The result enters this skill in a **plain** form: the competitor's thumbnails are grouped into **7 main art-style clusters**, and the number of thumbnails in each cluster is written: **painted digital · flat 2D drawing · classic oil painting · print / engraving / halftone · surreal / cosmic digital · comic / ink · photograph.** (This grouping is a grouping of Gemini's free-text descriptions, not the competitors' own labels; borderline thumbnails can fall in two groups.) The user gets an easy summary list. The detailed reading (type of person, portrait, symbols, color, text, common and different features, the relation to views, statistical verification) is a **separate, optional step**, run only if the user wants it.

## A5e. Gemini (`agy`) usage lessons and data traps
- The empty outputs were not a quota error but an **identity race when jobs were started in parallel**: run at most 2 jobs at a time, 20-30 seconds apart, with a unique output file, and give image jobs at least 300 seconds. The tool's logs are in its log folder under the Gemini config directory. If there is no answer after 3 minutes, do not wait: give the same job in parallel to another sub-agent (a small Claude model or ChatGPT).
- The "3 least viewed" that `fetch_competitor_data.py` puts in folders 16-18 may not be the real least viewed (it takes them from the channel's listed page); **look at the real views in `meta.json`** and do not trust the folder number. Likes, comments, date and duration are in `meta.json`; look there before writing "unknown".
- On the NexLev free plan there are 5 `youtube_channel_outliers` calls per 24 hours and no VPH is returned; the user accepts this.
- Clean up dashes with Python, not with sed (sed corrupts UTF-8).

## A6. Script analysis (from the transcripts)
- **Structure:** section order and durations, hook (first 30-60 seconds, real length), intro style, closing formula, transitions, fixed recurring elements, meditation/music interludes.
- **Content:** what it tells, how much it talks about the topic, warning sentences, number density, sources.
- **Voice/visual:** speaking speed, pauses, character count, ratios of image types. How many seconds of real video / images the competitor's latest video has; convert it into your own tool budget.
- **CTA count** (see A8).
- Something the user noticed while watching (for example "a small map animation at the start") is **measured** from the transcript and, if needed, from the video.
- **Common and different features between videos inside a single channel:** for each competitor, also extract the common and different features across the transcripts of its 15 videos (opening structure, case, repeating pattern, call to action, use of sources), not only across channels. The output goes into the script analysis file. At the end write only observations `[OBSERVATION]`, no causality.

## A6b. In-video visual and audio analysis (mandatory for every competitor; Gemini watches the video)
A transcript gives only speech; **visual structure, editing speed, motion, on-screen text, music and sound** come from watching the video. It goes into the competitor analysis, and the master's visual/audio section (B2 questions 7-8) rests on it.
- **Who watches:** a Gemini-based tool that really watches (picture + sound). Order: (1) `vidiq_video_watch` (vidIQ MCP, about 25 credits, asynchronous: get the result with `vidiq_job_poll`; videos up to 6 hours); (2) NexLev `watch_youtube_video_and_ask` (needs a paid plan; NO ACCESS on the free plan, tested); (3) **Local file + `agy` (Gemini CLI), no vidIQ and no credits, the recommended route:** `agy` cannot watch a YouTube link, but it sees and hears a local video file. Download the video at 480p with `yt-dlp` into a temporary folder (not into the notes), split it with `ffmpeg` into pieces of about 4:20 (a single 21-minute file timed out after 4.5 minutes), and have each piece watched separately with `agy -p "<prompt + file path>" --add-dir <folder> --print-timeout 600s` (each piece takes 3-10 minutes; write the output to a file; **run at most 2 jobs in parallel, 30 seconds apart, each job with its own folder and output file**: starting 7 jobs at once gave empty output because of an authentication race. If you script it: pieces of 260 seconds, 3 attempts per piece, `--print-timeout 600s`) and add each piece's offset to get real time. Transcript, description and thumbnails are read first; watching the video is not a last resort but it is expensive: **only the most viewed video** (and one mid and one least viewed if needed).
- **Prompt (fixed frame):** visual types and their time share (AI image, animation, diagram, stock, text only), cut rate (changes per minute; intro/middle/end), motion (zoom, pan, diagram animation), on-screen text, color and look (consistency with the thumbnail), music and sound effects, narrator (gender, accent, speed, AI voice or human), idea-to-visual mapping, 3 scene examples. A speech summary is **not requested**.
- **Check (two-tier):** the output's numeric claims (for example cut rate) are compared by the strong model with at least 2 frames (the thumbnail and one frame from the video) or a short clip; verdicts such as "AI voice" are labeled `[UNVERIFIED]`. The result is written to `<competitor folder>/video-visual-audio-analysis.md`.
- **A6b/A6c application lessons (from a run on 7 competitors, 61 pieces):** (1) A long job (about 2 hours) dies when the session restarts: **run it detached with PowerShell `Start-Process`**; the tool continues from the finished pieces without downloading them again (resume). (2) **Short last pieces** (under 3 minutes) have few table rows and cannot pass the success threshold; when it finishes, rerun with a relaxed threshold (for example number of `|` > 5); never leave a piece missing. (3) **First verify that the watched video really is the channel's most viewed video** (the watch page, or a data-verification note): the "01" folder of a data pack may not contain the channel's real top 4 videos (in one case the watched video was 5th; it was recorded as a limitation). (4) **Measure silence and music by code, in the main session** (`ffmpeg silencedetect` at -50 and -35 dB, `ebur128`); a small Claude model's silence counts were inconsistent and are not used until recounted with the same threshold. If music present or absent cannot be proven by measurement, write `[UNVERIFIED]`. (5) **Confirm the calls (subscribe / like / comment) against the transcript;** a call that Gemini saw but that is not in the transcript is `[UNVERIFIED]`. **Search lesson:** the pattern `grep -o '.{60}word.{60}'` misses matches at the start or end of a line (a subscribe call was wrongly judged absent, then corrected); in the transcript first use a simple `grep -n -i word`. (6) A mid-level summarizer may read the table **in shortened form**: ask "did you read all of it", and if not, have it read the whole file and correct the summary. (7) Merge the outputs per channel into `video-minute-by-minute-analysis.md` (piece headings with offsets); Gemini output can contain two tables in the same piece, so take only the first. (8) Gemini's times drift 5-10 seconds within a piece, and on-screen text quotes and cut counts are approximate; "x of 7 do this" is not causality (survivorship bias).

- **A6c Minute-by-minute analysis (one time, only the most viewed video):** the prompt asks for a table with one row per 10-15 seconds: time | what the narrator says (short paraphrase) | what is on screen (diagram type, objects, on-screen text, color, motion) | transition type; after each piece it asks for the number of cuts, how the visuals relate to the ideas, and the sound. The prompt says "write UNSURE when you are not sure". **Three-tier check:** (1) a cheap agent compares at least 10-14 frames with the real video (a mix from all pieces, plus the first 10 seconds and the last 30 seconds); (2) sound claims are measured by code (`ffmpeg` `silencedetect` / `astats`: if the noise floor between spoken words is around -80 dB, there is no music bed); (3) the strong model reads the whole file and lists inconsistencies between pieces, SUSPECT claims and an 8-point summary (hook, subscribe/comment call, closing, visual type, on-screen text, repeating structure, palette, cut rhythm). **Known limits:** at 1 frame per second a hard cut cannot be told from a fade, cut counts and dB figures are approximate, and transitions on a piece boundary are counted twice. Raw result: `<competitor folder>/video-minute-by-minute-analysis.md`; compiled findings go into the notes. **Lesson from the first run: a tool's claim "there is music and sound effects" was disproved by the second method (no music, no effects, dry narration). Never trust a single tool; compare two methods.**
- Output into the master: questions about the image/video ratio, the visual production method, the cut-rate target, music/sound effects and voice choice (B2 questions 7-8).

## A6d. Extracting rules from the minute-by-minute analysis (BEFORE the master is written, mandatory step)
After A6c is done and before the master is written (B3), the findings are handled one by one; the analysis is never just read and left.
1. **Sort into three boxes:** (a) the master already has it and the analysis confirmed it (only a "confirmed" note); (b) the master has it wrong and the analysis disproved it (fix it and delete the old claim); (c) a new mechanism (a rule candidate).
2. **Show the user:** for each rule candidate write "what the competitor does / how we would adapt it with our own brand", and the user chooses. The competitor's visuals, sentences, scenes and colors are never copied; only the mechanism is taken. The adaptation is made with the channel's own palette and drawing style; the aim is to avoid generic AI-slop look.
3. **Rule classes:** hook and promise structure (promise early, payoff in installments), CTA position and its own visual, closing, visual language (one sentence, one screen, one idea; color means concept; callbacks; draw the intuition, then refute it; visual type ratio), on-screen text, cut rhythm, sound (is there music).
4. **Write into the master:** visual, sound and editing rules are NOT mixed into the script master; they are written to a separate visual master file. Approved rules enter the relevant section of that master with the tags `[COMPETITOR A6c]` and `[USER <date>]`; a contradicting old rule is deleted completely (see B8). Rules that cannot be measured go to a checker item for the reviewers; measurable ones go to the check tool.
5. **Keep channel-specific decisions apart:** decisions that exist only for this channel and not in the competitor (for example a channel-specific production method) are not mixed into the competitor analysis; they stay on the channel's own page.
6. **Record it:** write a note listing which finding became which rule, which was not taken and why.

## A7. Reading-level test (mandatory for every competitor)
**Known limit (trial on a physics explainer channel):** NotebookLM's verbatim transcript has **no punctuation**; sentence-length ratios and readability formulas (Flesch) cannot be measured from it (the whole text comes out as one sentence). Fix, an automatic step of every analysis (not an optional note): do a punctuation repair first (Gemini/a cheap agent adds only punctuation and capital letters and changes no word); the repaired text is stored in a separate file (`transcript_punctuated.txt`) and the raw text is unchanged; then the strong model verifies by code that the word sequence is identical with `python -I -X utf8 scripts/verify_punctuation_repair.py transcript.txt transcript_punctuated.txt` (exit code 0 = identical, 1 = a difference, 2 = bad usage or a missing file; on a difference have it fixed and run the check again); only then measure the sentence numbers with `python -I -X utf8 scripts/measure_reading_level.py transcript_punctuated.txt --lang <en|de> reading-level-measurements.json`. Word-level measurements (unique-word ratio, most repeated words, word/character counts) need no punctuation and are measured from the raw text.
The competitor's scripts (the 2-5 most viewed videos) are tested with these measures:
- **By code `[MEASURED]`:** sentence-length ratios (short ≤12 / medium 13-24 / long 25+, average, longest; the sentence splitter is simple and miscounts abbreviations such as Dr. or e.g., so the ratios are approximate), average word length, **unique-word ratio**, **most repeated words**, long/heavy-word ratio, a readability formula suited to the language (EN: Flesch; DE: Wiener Sachtextformel).
- **Strong-model comment `[AI COMMENT]`:** CEFR level (**B1 / B2 / C1**), literary quality (story? novel? informative?), sentence-start variety, adjective use.
- **Compare with your own scripts** (if any): a "competitor / ours" table. If the gap is large, a master correction is suggested.
- **The decision is the user's:** the level suggestion is shown with the comparison; the chosen level and thresholds are written into the master and go into the Python checker.

## A8. CTA analysis
Count and place them in the competitor: how many, at which minute/percentage, which type (subscribe, comment, like, teaser, membership), tone (polite/command). If the competitor has none, ask separately how to weave them in. Output: a CTA table (type × position × count × tone). For the master's CTA section see B4.

## A9. Compare
- Most viewed vs never viewed (why; beware of selection bias).
- Your channel and scripts vs the competitor. The user's data: CTR, first-30-seconds retention, average view percentage, suggested videos, publishing day. Do not include old videos from a different line; keep the variables few.
- Output: **Situation in the competitor / Missing in the prompt / Fix.**

## A10. Channel setup (after the analysis + master are done, in this order)
1. **Channel name: 10 suggestions**, specific to the chosen language, **with translations**, derived from the competitor analysis (the pattern of competitor names, the main word). Search each suggestion on YouTube one by one (overlap): `vidiq_youtube_search` with `type: ["channel"]`, `limit: 3-4`, 5 credits per name; label the result "no exact match", "a close one exists (with its subscriber count)" or "in use"; a name that was not checked is plainly written "not checked". Most natural names come back taken: if the first round is eliminated, run a second round (for example in the style of the name the user liked). If a name contains a promise (for example "Without Math"), ask the user whether the promise fits the master's rules (the formula rule); "Made Easy / Simple" style names give the impression of a lesson channel, so warn if the channel is not one. A tagline can be chosen separately (the user picks). The user checks the @handle on YouTube. The user reviews and chooses. Record the choice in a decision note and in the master.
2. **Channel description:** from the competitor analysis (looking at the competitor's description) and **always containing the chosen vidIQ keywords**; 1000-character limit, with a translation, no warning/legal paragraph. Measure the count and the presence of the keywords with Python.
3. **Logo and banner:** first analyze the competitor's logo and cover/banner (color, figure, layout, safe area); download the logo with `python -m yt_dlp --skip-download --write-thumbnail --playlist-items 0 <channel link> -o <file>` and look at it. A common style block (STYLE) is repeated word for word in every prompt: the image has no text (name and tagline are added later), the banner keeps important content in the central 1546x423 safe area, color codes are suggestions (when the user chooses, they are written into the master's palette section), the competitor's main color tone is not used; only the mechanism of liveliness and contrast is taken from the competitor. **Gemini** (`agy`) writes prompts for 3 different versions (logo square, banner at YouTube size and within the safe area). The strong model checks the prompts.
4. **Image/video generator (for example Google Flow):** the prompts are prepared **in a new project, one by one**; ask for credit approval before generating. The user picks among the results.

### A10b. Video description and timeline
- Video description: each starts differently, 3-4 hashtags, keywords woven into the text (B7). **A timeline (timestamps) is made for every channel:** split the video into sections from the transcript/voiceover (SRT), write a timestamp and a title for each section (viewers click to jump). Never forget it.

## A11. Rules list, verified against the competitor
Produce a **rules list** from the analysis. For every measurable rule ask "does the competitor have this rule too, or did we make it up?" and write the **value measured in the competitor** next to it. A rule with no counterpart in the competitor counts as made up and is reported to the user. A feature absent from some of the competitor's videos is not mandatory; measure its frequency and set it accordingly. Fixed decisions given by the user (for example CTA timing) are kept despite the competitor data. **Do not move on to the master without the user's approval.**

## A12. Adding/removing competitors
If the user brings a new competitor, analyze it by style (script style, language level, thumbnail/title style). The user removes the ones that do not fit. Work out **why** the competitor's hook works. For an outside training video, make a "what we apply, what we do not" table; the user chooses.

---

## A13. Final scan of the master against the competitor analysis (after the master draft, before showing it to the user, mandatory)
Purpose: answer "is there something we did not put in, skipped or overlooked, and is there something else in common?" with code and an independent eye. Order: (1) **Gemini or ChatGPT (a small Claude model only if those are not enough)** lists every finding, rule candidate, gap and common/different feature in the competitor analysis (A2d, A4, A6, A7, A8, A9, B1b, video and thumbnail findings) and marks, with a line number, whether the current version of the master has a counterpart: PRESENT / MISSING / PARTLY; (2) **a mid-level agent** checks the list independently: were the "MISSING" ones really skipped or deliberately left out (a user decision, the no-copying rule, channel-specific), which of them matters, and is there a common point that is not on the list; (3) **the main session (the strong model)** does the final check, re-looks at samples, and gives the user an easy list: what was skipped, what was left out on purpose, what waits for a decision. Output: one scan file per channel in the competitor data folder. Nothing is written into the master without the user's approval.

# B. Prepare the master prompt

## B1. Precondition
**The master is not written until the competitor analysis is COMPLETELY finished:** A2d, A4, A5, A6, A6b/A6c/A6d, A7, A8, A9 and B1b/B1c (including keyword volume) must all be done and the open items closed; after the master draft, the A13 scan is run. The analysis is done, the rules list and the channel identity/genre are approved, the language decision is made. If the topic (title) list is ready, put it at the **very beginning** of the master.

## B1b. Topic selection: the competitor's Outlier and VPH scan (before the master, mandatory in every competitor analysis)
Terms: **Outlier** (how many times a video is viewed compared with its channel's typical video), **VPH** (views per hour).
**Outlier/VPH scan (the competitor's popular titles):**
1. **Pool:** for each topic title in the field, scan the **long explanatory videos of the last 12 months** with vidIQ (`vidiq_outliers`: `contentType: long`, `publishedWithin: oneYear`, `sort: breakoutScore` and, in a separate call, `sort: vph`; the results carry Outlier and VPH; if the language is not English, pass `language`; non-English searches cover only the last 6 months. `vidiq_youtube_search` is a raw search result, gives no Outlier/VPH, and is used only to find candidate channels or videos). Filter: not lessons/news/music/Shorts/face-on-camera hosts, and a reasonable channel size (for example under 1 million subscribers; a small channel's exploding video is more instructive).
2. **Ranking: selection is by Outlier score and VPH, not by views.** Two separate lists come out (top 10 by Outlier, top 10 by VPH); those in both come first. Views alone are never the criterion.
3. **Review:** the **top 10 competitor videos** in these lists are reviewed: title formula and ratios, hook (transcript), thumbnail, duration, channel size, topic and framing. The review follows A4-A7 (transcripts from NotebookLM); results are written to `<competitor folder>/popular-titles-review.md`.
3b. **Re-rank the whole topic list and all of the competitor's videos with the same score:** (a) for each topic on the list, run `vidiq_outliers` (keyword = main concept, `publishedWithin: oneYear`, `maxSubscribers: 1000000`, `minViews: 50000`, `limit: 8`) and write the strongest human-made evidence (Outlier + VPH) for the topic into the table; (b) fetch the competitor's most popular long videos with `vidiq_channel_videos` (`videoFormat: long`, `popular: true`; a limited number per call, not all) and sort them **by Outlier and VPH** (not by views), and extract the winning title patterns and the weak topics; (c) write a "score order" (very strong / strong / medium / weak) for the topic list into the master, with numbers kept fixed; the user chooses the order; (d) list the competitor's winning topics separately as backup candidates, never added automatically. The video types to leave out are decided from the channel identity card (in the trial on a physics explainer channel: AI-labeled sleep videos over 2 hours, celebrity clones, interviews and compilations). On a new video VPH is inflated, so read it only together with Outlier. Output: `<competitor folder>/topic-scoring-outlier-vph.md` (a "Verification" section is mandatory). Cost is about (number of topics + number of competitors) × 5 credits. The B1c measurement (`vidiq_keyword_research`) comes after this, only for topics scored medium or above, so the two measurement costs do not multiply.
4. **Back to topics:** the mechanisms and new sub-topics from the review are added to your own topic list **in your own framing** (principle 2: the mechanism is adapted, the wording is not copied); the user chooses what to add and the framing. The scan is redone on the fields (monthly, or every 10 videos).
5. **Check:** a cheap agent runs the scan; the strong model re-runs at least 2 queries and verifies, and opens at least 3 of the 10 videos and compares title/views/VPH/Outlier; for 3b it re-runs at least 2 topics and re-fetches at least 3 videos from the competitor's popular list. If the strong model took the data directly (no agent), it cross-compares with a second measurement (an earlier measurement or another query). The detail from the agent records is written into the "Verification" section.

## B1c. Main-concept keyword measurement and approval
- **Measure with main-concept words:** the competitor's winning videos are searched by **main-concept words**, not long-tail question patterns; candidate topics are measured first as main-concept words (vidIQ `vidiq_keyword_research`, `mode: research`, `includeRelated: false`, `limit: 1`, 5 credits per word; a cheap agent does it, the strong model re-runs at least 2 rows and verifies; "<750" is below the threshold, not zero).
- **Credit-free route:** (a) **Google Trends** (Classic Explore, Worldwide, 12 months, Web Search): in each group put one anchor term (for example the main word) with five other terms, read the values from the SVG bar heights and scale them with the anchor = 100; this is web search, not YouTube, and relative. (b) **The vidIQ web screen** (`app.vidiq.com/research/search?term=...`, Research > Keywords): monthly searches, Overall score, competition, trend; it spends no credits (verify with `vidiq_balance` before and after; a daily login reward can raise the balance); the page loads slowly, so wait 10 seconds for each term and read "Overall score ... Monthly searches ... Competition" from `document.body.innerText`; the screen does not state the region and period `[UNVERIFIED]`. (c) If the NexLev quota is full, use our own calculation as an Outlier proxy: relative views inside the channel (views / the channel's sample median) and daily views, by code, with the "least 3" folders and the listing error ("0 views") corrected first.

- **Eliminations:** topics whose demand falls, whose competition is very high, topics the competitor already covers (or only with a COMPLETELY different framing). Criteria: volume, a balance of competition/score, demand trend, absence in the competitor.
- Offer the user a topic + framing (a curiosity question); **the user approves the titles**; the approval record (their words and the date) is tagged in the master. Every title is searched on YouTube. The next lists of 10 are produced with the same process.

## B2. Pull the questions out of the competitor (the question-form method)
**Simple alternative (the user liked it):** a static HTML marking form (an artifact) with option buttons on every row (the first is my suggestion) and, at the bottom, a "Copy the result" button that the user pastes into the chat; no database is needed and Claude reads the answer from the chat.

**Format:** the form is published as a **web page** (an artifact with a database): each question is a card, the card shows the "measured in the competitor" value (yellow box), options (the first one is my suggestion) and a note field; answers save automatically and Claude reads them from there (`ArtifactData`). If a chat answer and a form answer conflict, **the later one in time is valid** and the conflict is reported to the user. Answers are written to a `master-form-answers` file, and each answer's source is labeled.
The detailed questions that make up the master are not asked from zero. The agent **fills the form from the competitor's data first**, then asks only the places that need the user's decision, **with options**. Each question has three columns: **In the competitor (measured) · My suggestion · The user's decision.** The question bank (for every new channel):
1. Topic scope, target audience, address form (you/we), the channel's identity.
2. **Language and level** (B1/B2/C1, showing the A7 comparison).
3. Duration and **character target** (competitor median + the user's target), number and length of sections.
4. Hook type and length, hook question, intro style.
5. Body structure, transitions, fixed recurring elements, closing formula.
6. **CTA matrix** (see B4).
7. Voice (female/male, speed, emotion tags), music, pauses. **Each channel has its own voice; a one-time, channel-specific choice.**
8. Image/video ratio, visual style, production tool and credit budget.
9. Warning sentences, forbidden and required words, forbidden topics, legal limits. **Not every channel has these; decide per channel, and where a channel has none, do not ask.**
10. Source and evidence order (a source link per section, nothing invented).
11. Title formula, thumbnail system, description layout (the user's approval in each part).
12. Originality: the overlap threshold with earlier scripts and the competitor, rotation rules (the closing/CTA text is never the same twice in a row).
13. Publishing rhythm, the first 10 videos list.
14. Which links stay with the user (hook, thumbnail, title) and which are automatic.
The user fills the form; unanswered items do not enter the master and are listed as "pending".

## B3. The master's structure
1. **Workflow, step by step.** "Start a new section" moves from the first section onward in order. The user can step in at any point and gets answered without losing the topic.
2. **Hook → the user says "hook ok".** The hook is always the user's manual approval. Then the script goes through the automatic quality loop below. **The script's final approval is also the user's, but only after all checks are done**; with the script the user gets a **check report** (which methods checked it how many times, how many update rounds, what was fixed in each round).
3. **Script quality loop (written inside the master):**

| # | Step | Who |
|---|---|---|
| 1 | Writing the script (the approved hook word for word inside) | **The strong-model writer agent** (master + section card). ChatGPT/Gemini/NotebookLM cannot write |
| 2 | Python check (paste the raw output) | `check_script`-style code |
| 3 | Master compliance check (unmeasurable rules, with line quotes) | **A separate zero-context second strong-model agent** |
| 4 | Fix (only the faulty part, surgical) | The writer |
| 5 | Re-check (2+3, a **new** checker every round) | code + a new strong-model agent; at most 3 rounds, otherwise the user is told |
| 6 | Originality: overlap with earlier scripts and competitor transcripts | code `[MEASURED]` |
| 7 | **Final judge** (runs the code itself, does not trust the reports) | **The strong model** → OK / RED |
If the final judge says OK, the script goes to **the user's approval** with the check report; if the user approves, it moves to voiceover. **It is not approved unless complete**; a rule violation cannot be a "warning", it is fixed. When the master changes, the **rule matrix** (each rule: measured by code / checked by the checker) is produced again; the checker gets the matrix instead of the whole master.
4. **Source approval (only if the channel requires sources; not every channel does):** source links for all sections, one bulk approval from the user, then the script.
5. **Output:** a downloadable .txt inside an artifact, ready for voiceover directly (no extra spaces/headings/notes), a fixed file name, saved over under the same name.

## B4. The CTA section in the master (the user's habits)
The master gets a **channel-specific CTA matrix**: type × position × count × tone × repetition rule. First write the value measured in the competitor (A8), then offer the user's habits as **suggestions**; the user chooses. Typical habits to offer:
- **Subscribe/follow CTA early:** after the hook, in minutes 1-3, at the latest in the first 5 minutes; polite, can be added to the end of a section. 3 times depending on the channel (start, middle, end) or fewer like the competitor.
- **Comment CTA as a question** that returns to the viewer's own life; in the first minutes or in the middle (minutes 5-7) a separate "question + comment" CTA.
- **Middle CTA:** a short block (about 10-12 seconds) after the emotional peak is over.
- **Closing:** short; no long CTA block, CTAs are spread through the video. A teaser pointing to the next video goes in if the competitor has one.
- **A CTA text is never the same in two consecutive scripts** (rotation); Python checks it.
- A CTA does not break the hook (no CTA in the first seconds unless the channel rule says otherwise).
- Even if the competitor has no CTA, the user's fixed timing decision is kept.
- Each CTA's position (percentage/minute) and count are written into the master **as measured**; the agent does not shift them on its own.

## B5. The Python checker
- **Every countable rule goes to code** (one tool for the script; a second tool for title/description/tags/section map/source file, run in stages); no manual checking or guessing. There is no violation that is passed as a "warning"; the one exception is rough marker rules (their status is CHECKER: the checker reads, and if natural it passes with a reason).
- **Thresholds are calibrated on the competitor:** measure the competitor's 3 most viewed videos with the tool's own functions; pick thresholds around the smallest/largest measured values. If a number the user gave conflicts with the competitor measurement, **the user's number stays** and the conflict is asked. Every threshold with no counterpart in the competitor is labeled `[SUGGESTION]` and listed to the user at the end of the master. The [COMPETITOR] values in the master are taken from the tool's own measurement (the measurement basis is written).
- **Mandatory arguments, no silent skipping:** the tool does not run without the reference (competitor transcripts) and the source page text (exit code 2). Overlap with the competitor and source texts has **zero tolerance**; with our earlier scripts the limit is the user's. Source page texts are saved word for word (not a summary, at least 300 words; the record made by the first-check agent is verified by the strong model on the live page with 3 passages). Repetition is checked by similarity (Jaccard); old versions of the same video do not count as "earlier scripts".
- **Edge cases are solved in the tool:** curly quotes, Unicode letters (Schrodinger), BOM, thousands commas, contraction pronouns (I'm, you're), abbreviation periods (Dr., e.g.), a hook that ends in a quote, arrow and math symbols, American spelling. For false alarms on real terms, an **exemption list** (updated with the user's approval); if the user gives their own hook, the hook rules count as EXEMPT (the values are reported).
- **The tool's self-test is mandatory:** from the competitor text produce an example script that "should pass"; apply a separate break to **every rule** (including the title/description tool); all breaks must be caught; when the tool changes, the self-test runs again (it must be OK).
- The code is not embedded in the master; it is a separate file; the raw output is pasted into the record every round (a separate file per round, history kept).
- **Idea similarity is measured both by reading and with Python; guessing is not accepted.** Code: sentence/n-gram similarity against earlier scripts, competitor transcripts and source page texts; reading (the checker): retelling of earlier scripts and of the competitor's story/example sequence.
- **The user gets a check report with every script:** which methods (code, independent checker, science accuracy, originality, judge) checked it how many times, and how many update rounds happened.

## B5a. Have your own AI write the checker (rule matrix + ready prompt)
The skill ships no ready-made checker, because the thresholds and rules belong to each channel. The checker is **generated per channel** by the strong model (never by ChatGPT, Gemini or NotebookLM) from the approved rules list, and it follows B5. Steps:
1. **Build the rule matrix first** (one row per rule; the checker gets the matrix instead of the whole master):

| Code | Rule | Checked by (code / checker) | Value measured in the competitor | Threshold | Source |
|---|---|---|---|---|---|
| M1 | for example characters and words | code | measured with the tool's own functions on the competitor's 3 most viewed videos | around the smallest/largest measured value | `[COMPETITOR]` or `[SUGGESTION]` |

2. **Give the strong model this prompt** (fill the brackets): *"Write the Python checkers for the rule matrix below: one for the script, and a second one for the title, description, tags, section map and source file, run in stages. Each is a separate file (never inside the master). Every countable rule is code; a violation is FAILED, never a warning (the only exception is the rough-marker rules, whose status is CHECKER). Required arguments: the competitor transcripts and the saved source page texts; without them the tool exits with code 2 and never skips silently. Overlap with the competitor and source texts has zero tolerance; with our earlier scripts the limit is [the user's number]. Source page texts are saved word for word (at least 300 words, not a summary). Repetition is measured by similarity (Jaccard); old versions of the same video do not count as earlier scripts. Solve the edge cases listed in B5 (curly quotes, Unicode letters such as Schrodinger, BOM, thousands commas, contraction pronouns, abbreviation periods, a hook that ends in a quote, arrow and math symbols, American spelling) and support an exemption list and a hook-exempt flag (when the user supplies their own hook, the hook rules count as EXEMPT and their values are still reported). Then write a self-test, covering both tools: build an example script from the competitor text that should pass, apply a separate break to EVERY rule, and make sure all breaks are caught. Print the raw output of every run."*
3. **Calibrate** the thresholds on the competitor with the tool's own functions (B5). A number the user gave stays, and a conflict with the competitor measurement is asked. Every threshold with no counterpart in the competitor is labeled `[SUGGESTION]` and listed to the user.
4. **Run the self-test** whenever the tool or the matrix changes; it must be OK before any script is checked. Paste the raw output into the record, one file per round.
5. **The checker is checked too:** the zero-context checker of B6 reads the code, tries it on small examples and looks for false alarms and misses.

## B6. The master itself goes through the same loop
**The strong model writes the master** (preparation data can be collected by NotebookLM/Gemini/ChatGPT; writing and checking are the strong model's). This line goes into the master: *"Scripts are written only by the strong model; checks are two-tier: the first check by Gemini/ChatGPT/Python, the final check only by the strong model; ChatGPT, Gemini and NotebookLM are only for data, summaries, first checks and raw drafts."* After the master is written and before it goes to the user, **at most 3 rounds**:
1. **Python master check:** characters, version/step-number sync, rule and matrix numbers, long/medium dashes, rule codes that are not in the tool or are in the tool but not in the master, commands and approval gates, label counts.
2. **An independent, zero-context strong-model checker** (NEW every round; it does not see the writer's reasoning or earlier reports): (a) internal contradiction and ambiguity (flow steps, gates, round/RED logic, the skeleton, rules breaking each other; tried by running the tool), (b) compliance with the user's decisions, (c) the source of competitor measurements (every [COMPETITOR] value is verified from files/the tool, unsourced thresholds are listed), (d) tool-matrix match (the code is read and tried on small examples; false alarms and misses are looked for; self-test coverage), (e) gaps, (f) copying from the competitor, platform policy and accuracy risk. Findings are classified CRITICAL / MEDIUM / MINOR.
3. **Fix:** the writer applies the findings (updates the tool, runs the self-test) and goes again with a **new** checker. After round 3, if no CRITICAL remains, the master counts as "ready to hand to the writer agent"; remaining MEDIUM/MINOR findings are shown to the user **item by item** as "acceptable?"; points that need the user's decision are gathered at the end of the master ("Points that need the user's decision"). A real example of these rounds: round 1 had 4 CRITICAL, round 2 had 3 CRITICAL, round 3 had 0 CRITICAL (13 MEDIUM, 22 MINOR).
3b. **Closeness-to-the-competitor scan (by code, 5-word sequences) and the last strongest-model check:** EVERY new example sentence that enters the master is scanned by code, with a 5-word sequence search, against the transcripts of all the competitor videos and against the compiled competitor notes; if there is a match, the sentence is changed and the result is written in the change note. After all checks are done, the master is checked **once by a strongest-model agent** (independent, holistic, does not touch the file); the user is asked **every time** before it is sent.

- **Copying and policy risk are shown openly:** following a format, resemblance to a single competitor, the platform's policy on mass-produced/unoriginal/synthetic content, music and image licenses. Remedy: an angle specific to each video, an everyday moment, a carrier analogy and a space for the user's contribution (the section card), repetition checks, the user's approval.
- **Science accuracy:** on contested or unresolved claims a hypothesis/interpretation sentence is mandatory; since the writer, checker and judge are the same model family, add a claim check with a **different model family (Gemini/ChatGPT)** and a comparison with the saved source page text.
- **What must enter the master's flow:** the section card and approval gates (card, hook, source, script, title, thumbnail), the round counter and the RED rule in one sentence, the checker inputs, the delivery files (a separate check file per round), the published-video record, the mechanism table (principle 2).

## B7. SEO section (goes into the master)
The keyword list from vidIQ **in the chosen language** (not the competitor's language) (word, Keyword Score, competition color) and the important title patterns in that language are **added** to the master:
- **In video descriptions** the keywords are woven into the text (the main word in the first 2-3 sentences).
- **At least 3 tags in every video.**
- **In every video the chosen words are used in changed combinations** (the same triple is not repeated in a row); Python checks it (tag count, presence in the description, no identical set in a row).
- Pulling the words and a per-video suggestion: the vidIQ MCP/extension (not Chrome, to save tokens); writing is the strong model.

## B8. Master hygiene and versions
When a new rule arrives, **delete the old one completely** (with the user's approval); do not write on top of it, and if there are many contradictions, rewrite from scratch. When a large master is shortened, confirm that nothing else was dropped. **Save every important version** (the user says "it broke" and you go back). The editing/video master is a **separate master and a separate project**. Additions to the master only with the user's approval.

---

# Report (at the end of every analysis)
What was done · measurements (raw) · **verification (which agent's job I checked with how many samples, result)** · problems · unverifiable items · one decision question. Use the output template below. Put a summary page into your notes under a meaningful name.

## Output template (what every competitor analysis contains)
Missing information is **never invented**; write `[UNVERIFIED]`.
- **A0. Channel identity card (the first section of every report, step A2):** the one-sentence result · evidence (hook, structure, narration style, language level, CTA percentages, visuals, voice, packaging) · **genre guess** (Evergreen/Cashcow/Trend/Hype, confidence, counter-evidence) · **competitor definition** (who is, who is not, who partly) · scan query and exclusion list · the user's approval.
- **A. Single-channel report (three layers):** 1 identity (name/ID, language, creation date, subscribers, video count, total views, upload frequency) · 2 genre (the A2 guess confirmed with A2b data, with reasons and approval) · 3 niche detail (sub-formats, audience, RPM and estimated revenue **with the calculation**) · 4 outlier videos (list, multipliers, **single-video concentration**: top-1 and top-4 share, the video that triggered growth) · 5 formula (title pattern, thumbnail language, hook, intro, closing, CTA placement, length, section structure) · 6 production route (script, voice, visuals/B-roll, editing, AI tools, time and cost of one video) · 7 competitors and clones (how many, how they differ, **clone network** sign) · 8 language gaps (which language lacks it, **RPM + competition + rising/slow new competitors by language**) · 9 risks (legal, copyright, policy, single-video dependence, slowing uploads) · 10 positives / negatives (separately) · 11 automation fit and script difficulty · 12 how we differ / structure to take and **what we will never take** (no verbatim translation) · 13 tool report (your analysis / what NexLev returned / what vidIQ returned, **separately, empty returns stated openly**) · 14 easy recipe (a 5-8 item summary of "how to do it easily") · 15 unverified items and **one decision question** (if any).
- **B. Script analysis card (per video):** title (+translation) · date · views/VPH/Outlier · length and characters · hook (first 30-60 seconds, what it does) · section order and minutes · intro sentence style · closing formula · CTAs (position/tone) · **sentence ratios** (short/medium/long, average, longest) · language level (B1/B2/C1) · unique and repeated words · literary quality · number/source density · music/pause pattern · **our structure** (a short note).
- **C. Comparison report (competitor vs ours):** same/different (table) · in the competitor but not in ours, in ours but not in the competitor · the **Situation in the competitor / Missing in the master / Fix** triple · viewed vs unviewed videos: likely reasons · suggested master changes (**one by one, with the user's approval**).
- **D. Multi-competitor list (a sheet):** rank · Outlier · VPH · total views · competitor channel · original title · target-language title · **real content summary** (nothing invented) · keywords · chosen/eliminated (why).
- **E. Report end:** 1 what was done (1-2 sentences) · 2 measurements (raw output, labeled) · 3 **verification** (which agent's job, who did the first check, how the strong model did the final check, how many samples, result) · 4 problems · 5 unverifiable items · 6 the one decision needed from the user.

## Files this skill produces and uses
(Quick mode's own output files are listed at the end of the Quick mode part.)
`<competitor folder>/` holds: `channel-identity.md`, `channel-identity-measurements.json`, `genre-curve-measurements.json`, `titles.txt`, `videos/`, `thumbnail_measurements.json`, `_summary.md`, `_notebook.json`, `popular-titles-review.md`, `topic-scoring-outlier-vph.md`, `vidiq-keywords.md`, `video-visual-audio-analysis.md`, `video-minute-by-minute-analysis.md`, the master-form answers, and the master prompt with its checker tools and per-round check files. The helper scripts are in this skill's `scripts/` folder.
