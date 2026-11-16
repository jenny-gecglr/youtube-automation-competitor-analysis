# Competitor analysis: ready-made prompts

These are prompts the author really used in competitor-analysis sessions, kept close to how they were written. Only the [bracketed] parts change. For the reason behind each rule see [method-and-rules.md](method-and-rules.md). Use them when you run the steps by hand or in another assistant; inside the skill, the workflow in `SKILL.md` already issues the equivalent requests.

## 1. One channel, deep analysis (the standard one, used most)
```
[channel link]

Think like a senior faceless-automation expert with 12 years on YouTube.
Analyze this channel for me in depth.
What is its type: cashcow, trend or evergreen? Analyze the niche in detail: competitors, production routes, language gaps, different opportunities, negatives, positives. Can it be done with YouTube automation, and if so how do I produce videos quickly by the easy route, and guide me in depth. How hard is the script to write? Which AI tools and editing methods were used, analyze that in depth too. First analyze it yourself, then with NexLev, then with vidIQ, and list whatever they show. Also describe an easy recipe summary of how it can be done.
```
Optional additions: *"can the same content style be done with another product/topic, give ideas, for example for [space]?"* · *"can a different channel be made this way? [your own idea], how would it be produced, what would it cost, how long does one video take; can it be done in CapCut or do I need to learn Adobe?"*

## 2. Language gap, and is there a competitor in that language?
```
Is there a language this channel does not exist in? Can you analyze it in detail with vidIQ?
Is there a competitor in [German] for this channel? Can you check in detail?
Can you give me the links of those channels so I can look?
Is [Portuguese] or [German] more sensible for this topic? Can you research it?
```
Speed variant: *"I need to open a channel quickly, can you also analyze it by 4-5 videos?"*

## 3. Title formula
```
Now sort all of this channel's titles one under another from most viewed to least viewed [channel link]
Let us pick the repeated words and extract the title format
```
Then: *"translate the [30] for [topic] too, **in exactly the same format**, write their translations next to them, but first analyze my main competitor's title formula and list the most repeated words."*
Check: *"can you check this list of 30 titles on YouTube? There must be NO overlap, EVER."* · *"there is a 100-character limit for titles, pay attention to it, then check on YouTube."*

## 4. Fetching and analyzing scripts
```
Now I want you to fetch the scripts of the competitor's 5 most viewed videos and give them to me as txt files, one by one.
```
```
Now I want you to analyze these scripts in great detail and produce a rules list.
```
```
I need the scripts of all published episodes of [channel]. Can you fetch all of them as txt with vidIQ? Name them from most to least viewed, put the view count at the start of the file name. Give them one by one.
```
Descriptions: *"now fetch the descriptions of these 5 videos please, I will download them the same way."*

## 5. Thumbnail analysis
```
Can you see all the thumbnails, or should I send you the images?
```
```
I will send 10 more. I want you to analyze all of them in minute detail. We will make the same style but according to our own titles.
```
```
The colors will be exactly like my main competitor's. I want you to describe [the competitor's thumbnails] exactly, one by one, that is, produce the exact prompts so I can make the same.
```
Thumbnail text: *"texts of [3] words to go on the thumbnails, matching the section; analyze them with the thumbnails, look, these are examples, there are names written on the collective image, match the titles with them, let us find a pattern. It must trigger emotion too; write their translations next to them."*

## 6. Language level and literary quality
```
Now I will give you the scripts of the [2] most viewed videos of my [2] competitors. Can you look at the language level of these scripts? What is the difficulty, B2 or C1? How much unique vocabulary is there, and how many repeated words? What is the literary quality of these contents? Like a story, like a novel, or informative; what is their narrative style? Then we will compare them with my scripts; I may need to fix my script-writing master.
```
Topic content: *"what exactly do the competitor channel's scripts tell, a short summary. Our channel's concept is [quantum]; how much do they talk about [quantum]? How many warnings like 'this is not science' do they give? Is it entirely spiritual? I am giving you the scripts, examine them, let us do a full deep analysis so I miss nothing."*
Intro/closing: *"I am not sure about the threat-sentence style in this intro; analyze the intros of the scripts, is there a firm rule?"* · *"can you analyze the closings from these scripts too? Is there a formula there?"* · *"is there a 2-minute meditation interlude in the competitor's videos? Does it not lower the views?"*

## 7. Viewed vs not viewed, against my own channel
```
Let us first compare the viewed and the unviewed videos; some videos got many views, some none; let us work out why, so I do not make the same mistakes.
```
```
Now analyze my channel; I made [3] videos, let us compare with them, then compare my scripts, and if it does not work out we add to our master prompt [channel link]
```
With data: *"now I will give you [the analytics]: the views graph, CTR, hook retention percentage, retention, suggested videos. In light of these, what do I need to do in the new video, let us think in terms of title and content, what can we add to our master?"*

## 8. Multi-competitor analysis (with a document)
```
Now we will start a new channel, but this time we will do it differently. Not on a single competitor: I prepared files for you by combining many competitors. In the document I copied the contents of those competitors' highest-outlier videos. Now, in order, very carefully, I want you to do the following:
1) analyze the document in minute detail, extract the patterns.
2) list all the YouTube video links attached in the file one under another and give them back to me
3) first of all find the video titles in the file and list all of them...
```
Ranking: *"sort the videos in the file I gave from most to least by outlier score and VPH, give it in SHEETS format. Columns: rank, outlier, VPH, total views, competitor channel, original title, [German] title, a short summary of what it really tells (nothing invented), keywords."*

## 9. Is anything missing in the master? (competitor scripts vs master)
```
I am giving you the competitor channel's scripts and also the names of the most viewed ones; take a look, did we miss anything?
```
Answer format that worked: **Situation in the competitor / Missing in the prompt / Fix.**
```
Since I will open this channel for [German] and [Germany], what must I really not do, how far can we stretch the script and how far must I narrow it; examine both this channel and the other competitor in [Germany].
```
```
Based on these, is there anything missing, wrong or different in my master?
```

## 10. Having the master prepared
```
To be able to write the script I want you to write a detailed master prompt, bound by the rules above; the character count must be between [30-32 thousand] and it must follow all the rules above without exception. Take our video title list into account, even include it, the whole list at the start of the prompt. The master prompt must be step by step, like a workflow. It must advance by getting my approval for the whole job step by step. Our titles are already ready; when I say "start a new section" it must begin with the first one and then continue in order. It must first write the script and then wait for my "script ok" instruction.
```
Extra rules (copy and paste):
```
All outputs it gives me must be inside an artifact and the script must be downloadable as txt. Since the script will be voiced, it must contain no unnecessary line breaks, spaces or paragraphs, no unnecessary text or headings in the script; it must be ready to copy and voice directly. Before giving me the script it must check all the rules once from start to end, and only if all rules are applied give it to me for approval.
```
```
After I approve the hook with "hook ok" it must move to writing the script itself, and after writing in line with all the rules, check all the rules inside itself before giving me output, and when everything is ok return the script as txt in an artifact.
```
```
Source content approval: it should research all sections in order in one go, list for each section at least 1 most popular source link one under another, take one bulk approval from me, then write the script. Name stories/facts must never be invented.
```

## 11. Channel setup (from the competitor)
```
Give [10] suggestions for the channel name and write their translations next to them. [Main word] must appear. Then can you search these words on YouTube one by one? What comes up?
```
```
First let us write the channel description; the competitor's is this [paste the description]; I want it according to the rules you understood but with a few emojis. It must not exceed 1000 characters. Write the translation too.
```
```
I am giving you an example so I can make my logo and channel image, my competitor's. Can you write a prompt for Google Flow so I can make similar ones for my channel? Do not skip the YouTube channel cover size, it must be exactly that size and with its safe areas. The colors will be the same as the competitor's.
```

## 12. Could I do the same as the competitor with my master?
```
I am giving you my 2-part master prompt and the competitor channel's information; compare them with my prompts, can we make a similar one to the competitor channel with my prompts?
```
The format of the answer: "yes/no + a table of differences in architecture, visuals and legal"; the 2-part master is given together.

## 13. What we can imitate + what we missed (list first, I will decide)
```
Now analyze this competitor in detail too, let us talk over it: what can we imitate from it, or what different thing is it doing that we missed; list them one by one and we will talk over them; do not change the prompt without asking me
```

## 14. Comparing several models (when you bring another AI's opinion)
```
Compare what ChatGPT said with what Claude said on the new competitor, list everything, the same ones and the different ones; I will decide whether to add to the master prompt accordingly
```
Note: this way mistakes like "zero competitors in this format in a country" and "8/10 score" were caught. Never turn a single model's answer into a rule; adding is the user's decision.

## 15. Audience question (a story decision)
When stuck between story/character options, ask: "which is stronger for a [US 50+] viewer?" Models tend to over-agree ("definitely stronger"); treat the answer as `[UNVERIFIED]` and compare it with a second model (prompt 14).
An optional method `[AI COMMENT]`: have the master scored against the competitor by component as a percentage (scenario, research, hook, editing). The numbers are subjective and are never used as the basis of a decision.
