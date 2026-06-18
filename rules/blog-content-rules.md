# Blog Content Rules

These rules apply to all blog writing, rewriting, and content generation workflows.

## Statistics & Sources

- Zero tolerance for fabricated statistics — every number must have a named source
- Inline citation format: `([Source Name](url), year)`
- Tier 1-3 sources only (see `rules/seo-quality-gates.md` for tier definitions)
- Minimum 8 unique cited statistics per 2,000-word article

## Paragraph & Sentence Limits

- Target paragraph length: 40-80 words
- Maximum paragraph length: **150 words** (hard limit — never exceed)
- Target sentence length: 15-20 words average
- Vary sentence length deliberately for natural rhythm

## Heading Structure

- Exactly one H1 per article (title only)
- H2s for main sections (60-70% should be questions)
- H3s for subsections — never skip heading levels (H1 → H2 → H3 only)
- Include primary keyword naturally in 2-3 headings

## Self-Promotion

- Maximum 1 brand mention per article (author bio context only)
- No promotional language — educational tone throughout

## Banned Patterns

### Em Dashes
- **Never** use em dashes (—) in blog content
- Replace with commas, hyphens (-), colons, or split into two sentences

### Banned Phrases (AI-Detectable Clichés)
- "In today's digital landscape"
- "It's important to note"
- "In conclusion"
- "Dive into"
- "Game-changer"
- "Navigate the landscape"
- "Revolutionize"
- "Seamlessly"
- "Cutting-edge"
- "Harness the power of"
- "Leverage" (as a verb)

## Visual Elements

- Include a visual element (image, chart, or callout) every 300-500 words
- No two consecutive visuals of the same type
- Every chart must be a different type (no duplicate chart types per article)
- All images must have descriptive alt text (full sentence, not just keywords)

## Answer-First Formatting

- Every H2 section must open with a 40-60 word paragraph containing:
  - A direct answer to the heading's implied question
  - At least one specific statistic with source attribution

## Community Footer

- Community footer is disabled by default
- Only show when `GEMINI_SEO_COMMUNITY_FOOTER=1` is set in environment
- **Never** include the footer in generated blog content, HTML, or markdown files
- Footer is terminal-only output after major deliverables
