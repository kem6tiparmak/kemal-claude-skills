---
name: humanizer
description: Use when Kemal invokes /humanizer, or asks to make a text sound human/less AI-generated, remove ChatGPT-isms or buzzwords, ban em dashes, or says a text "klingt nach KI/ChatGPT". Applies to both drafting a new text from scratch and editing/rewriting a text Kemal pastes in or points to a file. Works on German and English. Make sure to use this skill whenever Kemal explicitly names it or asks for text to sound more human/natural/less robotic — don't wait for him to spell out every rule, the skill already knows them.
---

# Humanizer

Kemal wants text that reads like a person actually wrote it, in whatever register was intended, business or casual. This is not about writing worse or dumber. It's about cutting the specific tics that give away LLM output: filler transitions, hedge-everything vocabulary, and a hard ban on em dashes. See `references/ai-tells.md` for the full list of words, phrases, and patterns to avoid, with before/after examples in German and English.

## Two modes

1. **Draft** — Kemal gives a prompt or bullet points, you write the text from scratch.
2. **Edit** — Kemal pastes text or points to a file, you rewrite it to fix the issues without changing the meaning or unnecessarily restructuring what already works.

## Register comes first

Before touching wording, figure out what register the text needs:

- **Business** (Altiparmak Event, OfferFlow, Projekt 2, client-facing): sachlich-professionell, warm, klar, keine Fachbegriffe ohne Not — see Kemal's global CLAUDE.md tone rules.
- **Personal**: gechillt, wie ein Kumpel.

Humanizing must land *inside* that register, not flatten it into generic "AI trying to sound casual" or generic corporate boilerplate. A sentence can be completely free of AI tells and still sound like a press release if the register is wrong. Read the context (who's this text for, personal vs. business) before writing a word.

## The hard rule: no em dashes

Never use an em dash (—), anywhere, for any reason. This is the one rule with zero exceptions — rewrite with a comma, a period (split into two sentences), a colon, parentheses, or just restructure the clause. Em dashes in AI-generated spacing (with spaces around them) are one of the most recognizable LLM tells there is, so this gets checked mechanically, not just by eye (see Self-check below).

## Everything else: judgment, not a blacklist

The vocabulary and phrasing patterns in `references/ai-tells.md` (delve, tapestry, "not just X but Y", "it's important to note that", vague attributions, copula avoidance, etc.) are *symptoms* of a deeper thing: LLMs default to the statistically safest, most generic phrasing available. The fix isn't swapping "delve into" for a synonym — it's asking "what would a specific person, with a specific opinion, actually say here?" and writing that instead. Use the reference file to recognize the pattern when you see it, then rewrite from the actual point being made, not from a thesaurus.

Don't over-correct into choppy, artificially blunt sentences either — that's just a different tell. Natural human writing still has some rhythm and varied sentence length.

## Self-check before returning the text

After writing a draft (new or edited):

1. Run `scripts/check_text.py` on the draft (pass the text via stdin or a file path) — it flags every em dash and every hit from the banned-phrase list mechanically, so you don't have to eyeball it.
2. Fix every em-dash hit. No exceptions.
3. For flagged vocabulary/phrases, use judgment: some hits are fine in context (e.g. "crucial" describing something genuinely critical isn't automatically wrong), but if several stack up in one draft, that's a sign to loosen up the phrasing generally, not just patch the flagged words individually.
4. Only return the text once the em-dash count is zero.

Match the input's language (German in, German out) unless Kemal asks for a translation or says otherwise.
