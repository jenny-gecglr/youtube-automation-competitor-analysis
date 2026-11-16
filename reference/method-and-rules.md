# Competitor analysis: the method, the questions and the rules

This file is the long form of the method behind `SKILL.md`. It was distilled from many months of competitor analysis work on different channels, including several very long analysis sessions and many one-off channel analyses. `SKILL.md` is the step-by-step workflow; this file explains the working philosophy, the standard questions, what to collect, the lessons learned and the mistakes that produced the rules. Read it when a rule in `SKILL.md` needs its reason, or when a step needs more detail (the full 15-point thumbnail list, the CTA rules, the rule-validation method).

Labels used here: `[USER]` the user's own decision or words, `[UNVERIFIED]` not fully confirmed, `[MEASURED]` counted by code, `[AI COMMENT]` the model's interpretation.

---

## 0. Philosophy (underneath every analysis)

1. **Walk the path of a channel that works; do not break its formula.** Cultural changes to a working formula are risks. "Do it the way the competitors did it" is the default.
2. **But never translate word for word.** What is taken from a competitor: topic, structure, formula, writing rules. What is never taken: sentences, sentence skeletons, scenes, signature phrases. Even in the hook: the competitor's formula, but entirely in your own sentences.
   - A native-language translation or summary made **for reading only** is allowed and is given on request.
   - **Characters, towns and proper names must differ from the competitor's**; run a name comparison when needed.
3. **Largest market, least legal risk.** Pick the language and country with the biggest market, but weigh the legal environment (for example health-claim rules in some countries make a format risky or impossible).
4. **What is not measured is a guess.** With data and tools at hand, no assumptions. Everything countable (words, characters, sentence-length ratios, repetition) is counted by code.

---

## 1. How a competitor is chosen and assessed

Standard questions for every new channel:
- **What is the genre: cashcow, trend or evergreen?** (SKILL.md A2)
- Analyze the niche in detail: competitors, production routes, **language gaps**, different opportunities, negatives, positives.
- **Can it be done with YouTube automation?** If yes, how are videos produced quickly and easily?
- **How hard is the script to write?**
- **"Describe an easy recipe for how to do it."**
- Which **AI tools and editing methods** are used?
- **Can the same content style be done with another topic (space, a product, a region)?**

Signals to watch while assessing a channel:
- **Growth speed:** a channel that opened on one date and had serious views three days later (a burst).
- **Few videos, many subscribers/views** (subscribers per video).
- **Dependence on one video:** if a single video carries 48-62% of the total views, it is not a true cashcow.
- **Clone network:** 20-90 clones using the same "About" text = a sold course/template, saturation.
- **Upload frequency and gaps** (for example a 62-day gap), **audience** (age, gender, country), **RPM.** If vidIQ does not show RPM: the monthly earnings shown in vidIQ divided by views.
- **Study the worst video too**, so the same mistakes are not made. Also find a **failed example**: "there is a channel like this, but it did not take off."
- **Legal/policy risk:** health-claim rules (for example in Germany and the EU), a doctor-avatar rejection, copyright/reused content (Content ID), YouTube's "fake AI content" policy, the demonetization risk of pseudoscience.
- **Language gap and competition:** "is there a language this channel does not exist in?" (vidIQ, in detail). List competitors in the target language **with links** and browse them yourself.
- **A "no competitors in the target language" claim is verified with a current search.** In one case an AI assistant claimed "zero competitors in this format in Germany"; a current search showed a competitor. A language gap finding is dated and written with its date.

### Scope of a competitor analysis (what limits it)
- **Work from the files and links the user gave.** Do not fetch whole channels that were not asked for. But when the user says "do not miss any detail, fetch all videos", fetch all of them.
- **If the user did not say "write a script", do not write one.** The job is to analyze the competitor and prepare the master.

---

## 2. The standard three-layer analysis order

Always shown separately in the output:
1. **First your own analysis** (the model's).
2. **Then NexLev.**
3. **Then vidIQ.**
4. **"List whatever they show"**: write exactly what each tool returned. If data did not come (credits ran out and so on), **say so openly; never invent it.**
5. The two tools' scores are computed differently (a NexLev outlier is not a vidIQ breakout): **report them side by side and do not treat one as correct.**
6. **The three layers work only where the NexLev and vidIQ tools are connected.** In an assistant without them, say that this layer is missing.

---

## 3. Data collection: what to have fetched

| Request | How it is asked | 
|---|---|
| Title list | Sort **all of the channel's titles from most viewed to least viewed**, one under another |
| Title formula | Pick the **repeated words**, extract the title format |
| Scripts | The scripts of the **5 most viewed videos**, one txt each, view count at the start of the file name; then **all** of them (most to least viewed) |
| Worst video | The script/summary of the least viewed video(s) too |
| Descriptions | The **descriptions** of the 5 most viewed videos, as txt |
| Thumbnails | Ask first: "can you see all thumbnails, or should I send them?" (in the skill the script downloads them) |
| Audience | Age ranges, gender, country |
| Time | Video lengths, upload frequency |
| VPH and outlier | Sort the videos by **VPH** and by **outlier score**; "are there high-outlier videos we did not put on the list?" |
| The competitor's latest video | Look at the latest script: **any change or difference?** Take 3 new scripts: any other pattern? |
| The competitor's own 15 best videos | Fetch them and **compare with your remaining videos**: "will my videos get watched? I want to be sure" |

Rule: **"As many as asked."** If 13 were requested, do not take only 6.
Rule: **Did you really read them?** "Could you read all scripts, or did you make up the summaries?" Confirm the count and content from the real file.

### Multi-competitor analysis
- The user collects the **highest-outlier videos of several competitors in a document** (content + links). In the skill, agents collect this themselves (SKILL.md A2b).
- Order of requests: (1) analyze the document in minute detail, extract patterns; (2) list all YouTube links one under another; (3) find and list the titles.
- The model's questions are answered by the user in bullets (topic scope, duration, voice, address form, language, first 10 videos).
- Ranking is **outlier + VPH together** ("the outlier must be high but the views high too, think of both").
- The list as a sheet: rank, outlier, VPH, total views, competitor channel, original title, **target-language title (separate column)**, **a summary of what it really says without inventing**, keywords.
- **Scope filter:** for example no sleep content, no superstition (love spells, salt rituals), no duplicate videos/topics.

---

## 4. Title analysis rules

1. **Extract the formula:** most viewed titles → repeated words → pattern (for example a "FOMO architecture" pattern, or "How People Live in ...").
2. **Translate into your niche, keep the format identical**: "translate the 30 for my topic, **in exactly the same format**, with translations next to them."
3. **A translation next to every title.**
4. **Search YouTube for every title for overlap:** "no title may match anyone's, EVER." Re-confirm in another session too. A channel in English was closed because of title overlap; that is the reason for this rule.
5. **Character limit: 100.** Fixed phrases (for example "4K Documentary") are not shortened.
6. **The channel's main words/place names in the title:** for example the best-known English name of a region; a famous figure's name.
7. **Title + thumbnail + hook match:** the promise on the thumbnail and title also appears in the hook.
8. **Variety:** titles starting with the same word back to back (for example a run of titles that all begin with "Ignore") must not sit next to each other; shuffle while keeping the views order. Titles should not all start with the same letter.
9. **A date/urgency may be in the title** ("September 9").
10. **A competitor's title may have been changed later** (for CTR): its title history matters.
11. **Keyword ratio:** how often did the vidIQ keywords appear in titles and descriptions?
12. **Re-search the competitor's titles one by one and be sure** ("search these 10 on YouTube again, let us be certain").

---

## 5. Thumbnail analysis rules

The thumbnail is the most important thing on a YouTube channel; CTR and views depend on it directly, so it has to be made flawlessly.

1. **Examine all thumbnails in minute detail:** composition, color, tone, **fullness**, dominance, figure, text. They are given 10 at a time.
2. **Palette identical to the competitor's** (the same in both channels). Neon balance: in the competitor's thumbnails **the whole composition has the same dominance and all colors are neon**. One object (a chest, a gem) dominating is a mistake.
3. **"Full and balanced"**, not empty or artificial ("like a cheap marketplace thumbnail").
4. **Describe the competitor's thumbnail "exactly, and produce the exact prompt"** (for an image generator such as Google Flow). **How closely to resemble the competitor is not fixed by a general rule; the user decides at every concept.** The AI does not set its own limit of "resemble this much"; it extracts every detail of each thumbnail and presents it (list 5A below). The competitor's image itself is never copied.
5. **Thumbnail text:** short (2 lines, 2+2 / 3+2 words), **matching the title**, **emotion-triggering**. "On a trend channel the viewer has to be triggered emotionally; with too short a text there is no emotional bond, it feels empty: *what should they get, what does this channel promise?*" Long text shrinks and cannot be read.
6. **One word in red** (the emphasized word at the end of a sentence); a red arrow and so on. Added by hand in Canva; it does not enter the master.
7. **Character reference** (a historical or mythological figure): faithful to the real look; add a reference image; extra research if needed.
8. **Production:** a **text-free image** with Google Flow, then the text is added separately; if a brand must show, link to the original packaging image.
9. **Channel logo and banner:** the competitor's is given as an example; the logo is **square**, colors like the competitor's, **vivid** (no darkening or haze), the channel name large at bottom center like the competitor's, the "follow" logo red, the banner at YouTube size and in the **safe area**. For the channel name, the figure (dragon, crow, mysterious man in a hoodie) must match the competitor's figure in strength.

### 5A. Thumbnail detail extraction list (mandatory in every analysis)
For every competitor thumbnail (at least the 10 most viewed, all if possible), write the items below one by one. One row/table line per thumbnail; at the end extract the "shared pattern" and the "exceptions". Numeric items are measured by code where possible.
1. **Format and ratio:** 16:9? resolution, edge margin, is there a strip/frame (for example a black strip on top).
2. **Composition:** where is the subject (left/middle/right, top/bottom), how many elements, gaze direction, foreground/middle/background, symmetry, where space is left empty.
3. **Fullness and balanced layout:** how much of the screen is filled, is the visual weight of the elements equal, does one element dominate.
4. **Color palette:** the 2-3 dominant colors, tone (neon/matte/pastel/dark), saturation, contrast, is there a red accent, light direction and color.
5. **Figure/subject:** who or what (person/animal/object/statue/creature), facial expression, pose, scale, camera angle (close-up, from above), a single subject or a conflict.
6. **Visual style:** oil painting, 2D flat, photorealistic, paper-craft, 3D, cinematic; whether the style changed over time (old/new videos).
7. **Text:** word count, line layout (2+2, 3+2), typeface kind (heavy serif/sans), upper/lower case, color, **which word is red**, position, size, outline/shadow, does it cover the image.
8. **Text content:** its relation to the title (repeats or completes), tone (command/statement/identity/question), "you" address, does it trigger emotion, is there a number. A foreign-language text gets its translation next to it.
9. **Extra elements:** arrow, circle, zoom box, logo, badge, icon, number.
10. **Title + thumbnail + hook match:** do the three give the same promise, does the scene shown on the thumbnail appear in the script.
11. **What the thumbnail-title pair triggers:** curiosity gap, fear, identity, benefit; the thumbnail's answer to "what should they get?".
12. **Consistency within the channel:** do the thumbnails look like a family (same skeleton) or is each different; when the template settled.
13. **Good vs bad performance:** put the most and least viewed thumbnails side by side; which item causes the difference (beware of selection bias).
14. **Production recipe:** an exact recipe for making this thumbnail (a text-free image prompt for the generator: an English prompt + an explanation), then the text in Canva.
15. **Unmeasurable/uncertain:** the AI's inference and what was measured are labeled separately (`[MEASURED]` / `[AI COMMENT]`); the user reads the emotion and decides.
**Output:** after this list, present a "what is shared / what changes" summary. **How closely to resemble is decided by the user together with the concept.**

---

## 6. Script analysis: what to look at

The competitor's most viewed scripts are read and the following items are extracted; the result becomes the **rules list**.

**Structure:** section order (which topic at which minute, for how long), the number of sections and whether it is fixed, the hook (first 30-60 seconds), the **intro sentence/style** (is there a threat sentence), the **closing formula** (a fixed triple, or variable), transition sentences, an element that repeats in every video (like a "typewriter" effect), is there a meditation/music interlude.
**Language:** **language level (B1/B2/C1)**, **unique words**, **repeated words**, **literary quality** (a story? a novel? informative?), sentence-length **ratios** (short ≤12 / medium 13-25 / long 25+; average; longest sentence), sentence-start variety, adjective use.
**Content:** what it tells, **how much it talks about the topic** (for example how much of a "quantum" channel is really about quantum), **warning sentences** ("this is not science"), mythology/historical detail, **number density**, sources.
**Engagement:** where the CTAs are, how many, in what tone (polite/imperative); subscribe / comment / teaser; how to weave them in if the competitor has none.
**Voice/music/visual:** the speech-music balance, the pause system, **only music + picture during voiceover pauses**, the competitor's real speaking speed, the real length of the hook (for example 1:17), the character count (with spaces), the drone/close-up ratio (80%/20%), a map animation (at which second), an epic closing.
**Converting into a production budget:** count how many seconds of real video and how many of images the competitor's latest video has, and convert that into your own tool budget. Example from a past analysis: the competitor had full video in the first 2 minutes (at least 12 x 10 seconds), quickly changing images in the middle and video in the last 2 minutes; in Google Flow a 10-second video cost 15 tokens, and the solution was 14 parts = 14 videos + 28 images.
**Noticing competitor patterns:** the user asks about things noticed while watching ("there is a small map animation at the start", "speech and music change"); the model **measures** it from the transcript.

**Comparison (very important):** the competitor's **most viewed vs never viewed** videos → "why, so I do not repeat the same mistakes"; **your scripts vs the competitor's** (language level, sentence ratios, closings); **within** your own scripts (the reason for a drop); the result: "is anything missing/wrong/different in the master?"

---

## 7. Comparing your own channel with a competitor (analytics)

The user brings their own data, the model interprets:
- The views graph, the drop **by publishing day**, reach, **CTR**, **hook retention (first 30 seconds) percentage**, **average view percentage / duration (retention)**, **suggested videos** (which audience the algorithm drops it to), the videos that bring followers.
- **Match videos with labels B1…Bn.** Order: good to bad.
- **Do not include old videos from a different line** in the analysis; judging them would be wrong.
- **Keep variables few:** when many things change at once it is hard to decide. Do not change many things at the same time; confirm with the retention graph.
- **Observation is not measurement:** what the user sees after months in this business counts as an "observation"; not everything has to be measured.
- Decision points: "at video 31 I will make one last analysis and decide to continue or stop."

---

## 8. From analysis to master prompt

The purpose of competitor analysis: **rules list → master prompt.** "If it will not be like that, why did we do all that analysis?"

1. **First the analysis + rules list**, approve, **then the master.**
2. **Master = workflow logic, step by step, the user's approval at each step,** but the user may step in and ask for something (the model answers without losing the topic).
3. It moves in order with the **"start a new section"** command (titles are prepared beforehand).
4. **First the hook (+ question), the "hook ok" approval, then the script.** Then: the model writes the script, **checks all rules inside itself**, and when sure gives the **single-piece final script as a txt in an artifact** (it does not ask approval for every section).
5. **The checklist runs in code (Python):** words, characters, sentence-length ratios, required words, language level. "The checklist must not guess." A rule violation **cannot be just a warning; it is fixed.**
6. **Output format:** inside an artifact, a **downloadable .txt**, the script **directly ready for voiceover**: no unnecessary line breaks, spaces, paragraphs, headings or notes, one piece.
7. **File name:** fixed (for example `CHANNEL1_Script.txt`, `CHANNEL1_Description.txt`), **saved over under the same name** (the name is not changed), with a date/version added (13092026).
8. **Master version discipline:** "Remove old-version explanations completely; if we remove something, it goes completely." The master's internal consistency is audited (step numbers, version, abbreviations, the same rule described differently in three places). When a big master is shortened, confirm that nothing else was dropped. A very large master → a separate content/sheet file.
9. **"Do not add to the master without my approval."** Sometimes the user says "I will do that manually".
10. **A separate master/project** for editing/video production (different names), so they do not collide.
11. **Source/research order:** a real **source link** for each section, **one bulk approval** from the user, then the script; the source list goes at the very bottom of the description. **Name stories and facts are never invented.**

---

## 9. Description, channel name and SEO

- **Channel name:** first suggestions (**with translations**), then **search YouTube one by one** (overlap), the main words appear in the name ("quantum and money for sure"; a famous figure's name). Research which figures are liked in the target country.
- **Channel description:** **look at the competitor's description and write like the competitor**; add mystery/curiosity; name popular names; **1000-character** limit (1048 = an error); with a translation; emoji (a set specific to the channel); no warning/legal paragraph.
- **Video description:** the variety of openings in the competitor's descriptions (each starts differently), **timeline/chapters** (section times from the script's word starts; the user corrects them after the voiceover), **3-4 hashtags**, keywords woven into the text. If chapters do not show, look for the reason.
- **The vidIQ keyword list** is used in titles and descriptions (including words from literal translations).

---

## 10. Behavior rules for the model (during analysis)

1. **No assumption or guessing.** With data and tools at hand, no guessing; if there is none, say "could not be verified".
2. **No inventing.** Not in numbers, sources, summaries or name stories.
3. **Stay in the scope asked.** The given file/link, the requested count.
4. **Do not decide or set rules on your own.** Offer options, the user picks.
5. **Every foreign expression gets a translation** (titles, thumbnails, descriptions, summaries); listed in section order.
6. **No long or medium dashes** (it shows an AI wrote it).
7. **Give numbers by code,** show the raw output; **really** run the checklist.
8. **No copying/rewriting** unless asked; if the user says "do not write, wait", wait.
9. **Do not repeat the same mistake:** when the user names a mistake once, make it a permanent rule and add it to the master **by asking**.
10. **Keep the user's observation separate:** the model's interpretation, the measurement and the user's observation are labeled differently.
11. **Ask few and clear questions.** Multiple-choice (Q/A) questions are preferred; explain a concept that is not understood in plain words (for example the user once asked what "concept assignment" meant).

---

## 11. Common mistakes (the reason for the rules above)

| Mistake | Result |
|---|---|
| Translating or closely rewriting the competitor's hook | Rejected, rewritten |
| Writing a script when an analysis was asked | The user was very angry |
| Fetching the channel's whole video list instead of the given file | "Work from my file" |
| A wrong count (6 instead of 13) | Rule: as many as asked |
| Suspicion of an invented summary | "Did you really read them?" |
| Title overlap (an English channel was closed) | Rule: search YouTube |
| Making the thumbnail far from the competitor ("cheap marketplace thumbnail") | Exact color / full / balanced |
| Inconsistency inside the master (step numbers, version) | Master audit |
| Counting a rule violation as a "warning" | "It needs a fix" |
| Not weighing the legal risk of a target country | A "what must I not do?" analysis |

---

## 12. Per-channel differences (same method, different choices)

The method is the same; each channel makes its own choices. Illustration of how the choices differed across four channels (labels are generic):

| Topic | Channel A | Channel B | Channel C | Channel D |
|---|---|---|---|---|
| Language | German | German | German | English |
| Length | 30 min | 31-32 min | 29-30 min | about 19-20 min |
| CTA | early comment CTA | subscribe + comment at the start/middle/end, comment in the first 5 min | follow CTA after the hook; middle CTA at minutes 5-7 | none at the start; 1 in the middle, 1 at the close |
| Teaser | `[UNVERIFIED]` | a next-video teaser exists | **none** (none in the competitor) | `[UNVERIFIED]` |

---

## 13. Validate the master's rules against the competitor (the most critical method)

The user tests **every rule in the master against the competitor.** The question pattern put to the model:

> *"Does the competitor have this rule too, or did we make it up?"*

Real examples:
- "Every paragraph at most 600 characters: where did we get that? Is the competitor's like that?"
- "Is the human-centered (People) rule in the competitor?" · "Are the drone sentences always like this in the competitor?"
- "Is the global domino effect in **all** competitor videos?" → if not, **it must not be mandatory**; do it if the competitor's video on the same topic has it.
- "Is flipping an expectation constant or rare in the competitor?" → measure it and set the **frequency** accordingly (result: only at important transitions, 4-5 in total).
- "Is 'two long sentences cannot come back to back' the same in the competitor?" · "What is the most long sentences in a row in the competitor? Compute it and add it as a rule" (since our text is shorter, the ceiling is 5, not 7).
- "Check the 8 unsourced rules against the competitor one by one and decide what to remove. The CTA timings I gave stay as they are."

**Rule:** every measurable rule that enters the master must have its "**value measured in the competitor**" written (for example "152 sentences: short 19.1% / medium 50% / long 30.9% / average 22.2 words / longest 58"). A rule with no counterpart in the competitor counts as **made up** and is reported to the user. **Fixed decisions the user gave (CTA timing and so on) are kept despite the competitor data.**

## 14. Take ratios from the competitor, then verify by code
- The competitor's **thumbnail and title ratios** are extracted by code: command/prohibition ratio, "you" address ratio, titles with numbers, word count, tone (command / statement / identity). Goal: "the ratios here should be like the competitor's in ours too."
- **The measurement measures similarity, not emotion.** The user reads the emotional load and decides ("how will I be sure?" → put them side by side with the competitor's thumbnails).
- **The user's decision outranks the measurement:** the target for titles with numbers was 33% and 28% came out; the user said "that is too many, cut it to 5" and found titles like "13 habits" boring.
- **One word in red on every thumbnail** (the most important word in the sentence, for emphasis) is a firm rule.
- If a thumbnail text feels meaningless/empty (for example "You love a picture"), it is **rewritten**; weak ones are scanned across all, not only where the user pointed.

## 15. Every countable rule goes to Python
- "**All countable, measurable rules must be checked from Python, I want no hallucination at all.**" "Not by hand, add it to the tool."
- When a rule is added, the checking tool is updated too; bugs in the tool are fixed (for example a search for "Freud" catching "Freude" (joy): use a word boundary `\bfreud\b`).
- **Idea similarity cannot be measured**, code cannot do it: say "similar / not" by **reading** earlier scripts. If there is no earlier script, ask the user for one.
- Last step before delivery: a **competitor scan** (forgotten once): what is shared with the competitor, sentence lengths, vocabulary, the core of the topic, "how original are we".
- **Do not embed the code in the master.** (The check code was 27% of one master; it runs as a separate file and the master dropped to about 70 thousand characters.)

## 16. Evidence and source mapping (when a channel cites sources)
- Match each video to the relevant **book/diary** (books can repeat); in the hook (first minute) one sentence: "X wrote this in [work]"; in the description: "the concept in this video was inspired by X's work"; the quoted sentence must **match the video's title and summary**.
- The mapping is **not invented.** The question "on what basis did you match this, explain" comes; being verified from even one source is enough (not all books are online). A mapping that does not match the title/summary counts as "junk" and is **redone from scratch.**
- The unverifiable part is not deleted; the "X says" part is taken out and worked into the text. The source requirement is written as "optional" and Python checks it.
- **Do not eliminate keywords too sharply:** for example a "promise of healing" must not appear in the script, but if the author's core is healing, popular books (for example a famous work) are not eliminated; the user takes what they mark.

## 17. Adding and removing competitors, and outside sources
- The user keeps finding **new competitors** (fast-growing, similar in style, a famous channel in the home language) and says "analyze in detail". The analysis question is **style-focused:** "How are the scripts? Hard? What style are the thumbnails/titles? Does it tell a story or give information? Is the language level C1 or B2?" (the model once looked only at the surface, and the user corrected: "that is not where you should look".)
- **Eliminated** if it does not fit the target style/niche line ("this channel is about a different subject, forget it"). Elimination is the user's decision.
- **Translate the titles into the target language and search YouTube**: is there an equivalent (is the translation occupied or empty).
- **Verify an advantage in your own channel:** a liked competitor's visual style (an oil-painting living picture) is compared with your own visuals, with the logic "if it is original, the chance of success is high".
- **An outside training video/analysis** (one the user found): "can it be useful for us, **what do we apply, what do we not** in our channel?" → compare item by item; the user decides one by one (for example "baseline/median and ceiling calculation", "do not copy a single outlier, ask WHY the format works", "the hook's 4 questions: Promise, Proof, Plan, Persona", "who the hook is for"). A balanced acceptance: "do not frame everything with a single rule, let some videos have it"; "let us not repeat the same thing back to back, it gets boring".
- **Analyze why the competitor's hook works** (not the format, the reason): "we could not fully work out why the format works" → ask for extra analysis.

## 18. Master hygiene and version management
- **When a new rule arrives, delete the old one completely.** A master must not grow endlessly; writing on top of it makes "soup". If there are many contradictions, **rewrite from scratch.**
- Do not write something unwanted and then say "not applied": **delete it completely.**
- Contradiction scan: the same rule described differently in several places, lost header/footer version sync, shifted step numbers, a section that does not hold within itself, example sentences that use a pattern the master forbids, an example template that is too close to the competitor's sentence (copy risk).
- If the user says the master "broke", they **go back to the earlier version** (they keep the old big version); so save every important version.
- File/title/description layout: at the start of each description file the title + its translation + thumbnail alternatives + their translations; for each video **1 final title + 2 thumbnail alternatives**, in an artifact, **all at once** (not piece by piece in the conversation).

## 19. The rule about not forgetting context
The user can work on the same analysis for hours. "We have been analyzing this for hours and you are still making nonsense searches in vidIQ", "take the competitors file, did we prepare it for nothing, everything is there." → the model **first looks at the file the user gave and the earlier decisions**, then runs a new search. Never ask the same question twice.

---

## 12A. CTA (call to action) rules

### General CTA rules (all channels)
1. **Count and position the CTAs in the competitor:** how many, at which minute/percentage, which type (subscribe / comment / next-video teaser / like / membership).
2. **Tone:** polite or imperative; the competitor's tone is measured and the user picks according to the channel's identity.
3. **A comment CTA is asked as a question** and returns to the viewer's own life; if possible a short comment keyword goes with it.
4. **A long closing block** (subscribe + like + membership + next video back to back) is not written unless the channel's rule allows it; CTAs are spread through the video.
5. A CTA does not break the hook: if there is no CTA in the first seconds, none is pushed in (unless the channel rule says otherwise).
6. Even if the competitor has no CTA at all, the user's fixed timing decision is **kept** (competitor data does not override those fixed items, section 13).
7. The **position (percentage) and count** of each CTA are written into the master as measured; the AI does not shift them on its own.

### Channel-specific CTA (examples of how choices differ)
| Channel | CTA layout |
|---|---|
| Channel A | an early comment CTA; 5-6 spread CTAs, a long closing block is forbidden; the comment CTA at about 25-35% of the video `[UNVERIFIED: exact minutes need confirming]` |
| Channel B | subscribe + comment at the start, middle and end, a comment within the first 5 minutes; a next-video teaser exists |
| Channel C | an early follow CTA after the hook; a middle CTA at minutes 5-7; no teaser |
| Channel D | none at the start; 1 in the middle, 1 at the close; a comment question is mandatory (ask in section 5, repeat in 6) |
| Channel E (an archived one) | the middle CTA: a short block of 10-12 seconds after the emotional peak is over; the close: "don't miss the next story" |
