# anti-slop

A reference list of AI writing patterns. Words, phrases, and structural tells that show up far more often in LLM output than in human writing.

"Slop" is what people started calling text that reads like unedited ChatGPT output. Low information density, predictable structure, vocabulary no human would reach for. [Macquarie Dictionary named it their 2025 word of the year.](https://www.macquariedictionary.com.au/word-of-the-year/)

The lists below come from working with LLMs daily and observing what they consistently reach for, cross-referenced with frequency analysis from [slop-forensics](https://github.com/sam-paech/slop-forensics) and [EQ-Bench](https://eqbench.com/slop-score.html). Not every use of these words is wrong, but clusters of them are a dead giveaway.

There's also a small script you can run on any file:

```bash
./slop-check.py your-draft.md
```

And machine-readable versions of all the word lists at [`data/`](data/) if you're building a linter, editor plugin, or CI check.

## Banned words

### Tier 1: kill on sight

These almost never show up in casual human writing. If you see one, rewrite the sentence.

| Slop word | What a human would write |
|---|---|
| delve | dig into, look at, examine |
| utilize | use |
| leverage (verb) | use, take advantage of |
| facilitate | help, enable, make possible |
| elucidate | explain, clarify |
| embark | start, begin |
| endeavor | effort, try |
| encompass | include, cover |
| multifaceted | complex, varied |
| tapestry | (just describe the actual thing) |
| testament ("a testament to") | shows, proves, demonstrates |
| paradigm | model, approach, framework |
| synergy / synergize | (delete the sentence and start over) |
| holistic | whole, complete, full-picture |
| catalyze / catalyst | trigger, cause, spark |
| juxtapose | compare, contrast, set against |
| nuanced (as filler) | (cut it. if the thing is nuanced, show how.) |
| realm | area, field, domain |
| landscape (metaphorical) | field, space, situation |
| myriad | many, lots of |
| plethora | many, a lot |
| whilst | while |
| ever-evolving | changing, growing |

### Tier 2: suspicious in clusters

Fine on their own. Three in one paragraph and you've got a problem.

| Slop word | Plainer alternative |
|---|---|
| robust | strong, solid, reliable |
| comprehensive | complete, thorough, full |
| seamless / seamlessly | smooth, easy, without friction |
| cutting-edge | new, latest, modern |
| innovative | new, original, clever |
| streamline | simplify, speed up |
| empower | let, help, give (someone) the ability |
| foster | encourage, grow, support |
| enhance | improve, boost |
| elevate | raise, improve |
| optimize | improve, tune, tweak |
| scalable | grows with you, handles more load |
| pivotal | important, key, central |
| intricate | complex, detailed |
| profound | deep, significant |
| resonate | connect with, hit home |
| underscore | highlight, stress, show |
| harness | use, put to work |
| navigate (metaphorical) | deal with, work through, handle |
| cultivate | build, grow, develop |
| bolster | strengthen, support |
| galvanize | motivate, push, rally |
| cornerstone | foundation, basis, core |
| game-changer | (be specific about what changed) |

### Filler phrases

Verbal tics. LLMs insert them like nervous speakers say "um." Zero information. Delete all of them.

| Phrase | What to do |
|---|---|
| "It's worth noting that..." | Just state the thing. |
| "It's important to note that..." | Just state the thing. |
| "Importantly, ..." | Just state the thing. |
| "Notably, ..." | Just state the thing. |
| "Interestingly, ..." | Just state the thing. (If it's interesting, the reader will notice.) |
| "Let's dive into..." | Delete. Start with the content. |
| "Let's explore..." | Delete. Start with the content. |
| "In this section, we will..." | Delete. The heading already says this. |
| "As we can see..." | Delete. They can see. |
| "As mentioned earlier..." | Delete or just reference the thing directly. |
| "In conclusion, ..." | Delete. The reader knows it's the end. |
| "To summarize, ..." | Delete or just... summarize. |
| "Furthermore, ..." | and, also, (or just start a new sentence) |
| "Moreover, ..." | also, and, plus |
| "Additionally, ..." | also, and |
| "In today's [fast-paced/digital/modern] world..." | Delete the whole clause. |
| "At the end of the day..." | Delete. |
| "It goes without saying..." | Then don't say it. |
| "Without further ado..." | Delete. |
| "When it comes to..." | Just talk about the thing. |
| "In the realm of..." | in |
| "One might argue that..." | Argue it or don't. |
| "It could be suggested that..." | Say it or don't. |
| "This begs the question..." | Almost always misused anyway. Delete. |
| "Cannot be overstated..." | It probably can. State the specific impact instead. |
| "Is absolutely essential..." | "matters", "you need this" |
| "A [comprehensive/holistic/nuanced] approach to..." | an approach to |
| "Not just X, but Y" | Restructure. This is the #1 LLM rhetorical crutch. |

## Structural patterns

Bad vocabulary is easy to catch. Bad structure is harder. These are the patterns that give AI writing away even when the individual words are fine.

### The topic sentence machine

LLMs default to a rigid paragraph template: topic sentence, elaboration, example, wrap-up. Every paragraph. Same rhythm. Human writing doesn't work this way. Sometimes the point comes at the end. Sometimes a paragraph is one sentence. Sometimes there's no thesis statement at all.

Slop:

> Error handling is a crucial aspect of software development. When errors occur, they can lead to unexpected behavior and poor user experience. For example, an unhandled null pointer exception might crash the entire application. Therefore, implementing proper error handling is essential for building reliable software.

Human:

> Your app will crash. Not "might crash" -- it will. The question is whether you wrote a try/catch or whether your user gets a stack trace at 2 AM.

The human version has a voice. The slop version could be about anything.

### List abuse

LLMs love bulleted lists. They use them where prose would be clearer, where a table would work better, and where a single sentence would do. Red flags: every item starts with the same grammatical structure ("Ensures...", "Provides...", "Enables..."), the list substitutes for actually explaining something, nesting goes 3+ levels deep, or there are exactly 3 or 5 items (LLMs gravitate to these counts).

### Symmetry addiction

Three pros, three cons. Five steps. Equal-length sections. Real writing is lumpy. Some sections are long because the topic is complex. Some are two sentences because that's all there is to say. If every section of a document is roughly the same length, something's off.

### The hedge parade

LLMs hedge constantly: "can", "may", "might", "could potentially", "it's possible that." Human experts state things. If you know it, say it. If you don't, say you don't.

Slop: "This approach may potentially help improve performance in some cases."
Human: "This is faster." (or "We haven't benchmarked this yet.")

### Transition word addiction

Read the first word of every paragraph in a piece of text. If you see "However... Furthermore... Additionally... Moreover... Consequently... Nevertheless..." it's AI. Human writers start paragraphs with the actual subject.

### The "not just X, but Y" construction

The single most overused rhetorical pattern in LLM output. Shows up in nearly every model's top trigram lists per [slop-forensics](https://github.com/sam-paech/slop-forensics). Every time you see it, kill it and rewrite the sentence.

Slop: "This isn't just a tool -- it's a paradigm shift in how we think about development."
Human: "This tool changes how we develop."

### Em dash overload

One or two em dashes per page is normal. Five per paragraph is an LLM trying to sound dramatic. Where a human would use a comma, parentheses, or just write two sentences, LLMs reach for the em dash.

### Sycophantic openings (aka "glazing")

Responses that start by praising the question: "Great question!", "That's an excellent point.", "Absolutely! Let me explain...", "You raise an important consideration." Collins Dictionary shortlisted "glazing" -- excessive AI flattery -- for their 2025 word of the year. If text starts by praising you before answering, a model wrote it.

### The false-depth pattern

How LLMs fake being smart: (1) restate the problem in fancier words, (2) list obvious considerations, (3) conclude with "it depends" or a vague call to action. None of it adds information. Real depth comes from specifics: data, edge cases, tradeoffs, things that went wrong. If you can swap the topic and the text still works, it's slop.

## Tone by context

Different contexts need different fixes.

**Academic writing** -- Dense, precise, every claim cited. No performative enthusiasm. State findings directly. Short sentences. "We observed a 12% reduction in loss (Table 2)" not "We observed a significant and noteworthy reduction." If you're uncertain, say so explicitly instead of hedging with "may" and "might."

**Blog posts** -- Has a voice. Opinionated. Uses "I". Reads like a person wrote it. Start with the punchline, not three warmup paragraphs. Use contractions. Have opinions. Be wrong sometimes. Perfect balance on every topic is a tell.

**READMEs** -- Get the reader from zero to running as fast as possible. Show a code example in the first 10 lines. "Requires Python 3.10+" not "This project leverages cutting-edge Python features." Link to docs for everything else.

**Tutorials / notebooks** -- Like talking to a colleague at a whiteboard. "The loss is still garbage. Let's try dropout" not "The results suggest that further optimization may be beneficial." Show your reasoning, not just results. Leave mistakes visible.

## How AI detectors work

What tools like [Pangram](https://pangram.com) and [GPTZero](https://gptzero.me) actually measure, so you understand why slop gets flagged.

**Statistical signals** -- Low perplexity (text is predictable, each word is what a model would most likely pick next; perplexity below 50 = red flag), low burstiness (sentence lengths are all roughly the same instead of mixing short and long), uniform entropy (steady information density instead of the dense/sparse variation humans produce).

**Vocabulary signals** -- Slop word frequency (60% of EQ-Bench's composite score), low vocabulary diversity measured by MATTR, trigram overrepresentation (three-word phrases that appear way more in AI text, 15% of EQ-Bench score).

**Structural signals** -- Repeating paragraph template, list-heavy formatting, balanced section lengths, opening/closing formulae ("In this article..." / "In conclusion..."), no personal markers (no "I", no anecdotes, no experiences, no mistakes).

Pangram specifically uses a deep learning classifier trained on ~1M documents (not simple perplexity heuristics). It tokenizes input, creates embeddings, runs a classifier that outputs human/AI/AI-assisted probability, and highlights specific phrases with elevated AI probability.

**Limitations** -- All detectors have non-trivial false positive rates. Short text (<100 words) is unreliable. Newer models are harder to catch. Non-native English writers get flagged more often (perplexity tools are biased). Edited AI text is much harder to detect. Experienced humans spot AI text ~90% of the time; tools do worse.

## The anti-slop checklist

A [standalone version](checklist.md) is available for quick reference.

**Words** -- Search for Tier 1 words (replace or delete every one). Search for Tier 2 words (3+ in one paragraph = rewrite). Search for filler phrases (delete all). Count em dashes (more than 2 per page, cut some). Count "not just X, but Y" constructions (kill them).

**Sentences** -- Check the first word of every sentence (all transitions = rewrite). Check sentence length variation (all 15-25 words = mix in short and long ones). Find hedging chains ("may potentially", "could possibly" -- state it or don't).

**Paragraphs** -- Same template every paragraph? Break the pattern. All the same length? Vary them. No voice? Add one.

**Structure** -- Sections suspiciously balanced in length? Real topics aren't symmetric. List abuse? Convert some to prose. Throat-clearing opener? Cut to the point. Generic ending? End with your actual last point.

**The smell test** -- Read it aloud. Does it sound like a person or a press release? Would you be embarrassed if someone asked "did AI write this?" Does it say anything specific, or could you swap the topic and it still works? Is there a single surprising sentence? Human writing surprises. Slop never does.

## Sources

- [slop-forensics](https://github.com/sam-paech/slop-forensics) -- frequency analysis of overrepresented words in LLM output
- [EQ-Bench Slop Score](https://eqbench.com/slop-score.html) -- composite metric for AI text patterns
- [Pangram](https://pangram.com) -- AI detection via deep learning classifier
- [GPTZero](https://gptzero.me) -- perplexity and burstiness-based detection
- [Macquarie Dictionary](https://www.macquariedictionary.com.au/word-of-the-year/) -- named "slop" 2025 word of the year

## Contributing

Found a slop pattern we missed? See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE)
