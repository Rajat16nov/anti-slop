# Contributing to anti-slop

Want to add a new slop pattern? Fix something wrong? Good.

## How to contribute

### New slop word or phrase

Open an issue using the "New slop pattern" template. Include:

1. **The word or phrase**
2. **Evidence it's overrepresented in AI output** -- a link to slop-forensics data, EQ-Bench scores, or your own frequency analysis. "I see it a lot" is a starting point, not proof.
3. **What a human would write instead** -- plain alternatives.
4. **Which tier it belongs in** -- Tier 1 (kill on sight), Tier 2 (suspicious in clusters), or Tier 3 (filler phrase).

### New structural pattern

Same deal. Describe the pattern, show a before/after example, explain why it's a tell.

### Corrections

If something in the guide is wrong or misleading, open an issue or PR. No need for a template -- just explain what's wrong and why.

## Pull requests

- Keep changes small and focused. One pattern per PR.
- Match the existing tone. This guide is direct and opinionated. Don't soften it.
- Don't add slop to the anti-slop guide. We will notice.

## What we don't want

- Subjective style preferences disguised as slop patterns. Slop is about statistical overrepresentation in AI output, not personal taste.
- Words that are perfectly normal in human writing but happen to also appear in AI output. The bar is: does this word appear significantly more often in LLM text than in comparable human text?
- AI-generated contributions. Yes, we see the irony. No, we don't care. Write it yourself.
