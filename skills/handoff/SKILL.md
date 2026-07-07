---
name: handoff
description: Prints a ready-to-copy handoff prompt summarizing the current conversation so the user can paste it into a fresh Claude Code session and keep working there. Only ever trigger on the explicit /handoff command — never invoke automatically mid-conversation, this must not act like context compaction.
disable-model-invocation: true
argument-hint: "Optional: what should the next session focus on?"
---

Produce a handoff prompt for the current conversation. The user will copy your entire reply and paste it as the first message in a brand-new session — so your reply must contain ONLY the handoff block, nothing before or after it (no "Here's your handoff:", no closing remarks).

This is not a summary of the conversation for a human to read. It is an instruction written *to* the next Claude instance, telling it what's already true and what to do next. Write it that way — direct, addressed to the reader who will act on it.

## Why this exists

`/compact` re-reads and summarizes the entire transcript automatically, which is slow and tends to lose the details that actually mattered while keeping filler. This skill instead does one fast, targeted pass over what's relevant right now — you decide what's worth carrying forward, not a generic compression algorithm. Nothing gets written to disk; the user doesn't want a file to go dig up later, they want text they can grab and paste immediately.

## Before writing: redact

Strip any API keys, tokens, passwords, or other credentials that appeared in the conversation. Replace with `[REDACTED]`. If personal data (addresses, phone numbers, etc.) isn't relevant to continuing the task, leave it out rather than repeat it.

## Template

Fill this out based on the actual conversation. Skip a section entirely if it has nothing to say — don't write "None" placeholders.

```
Handoff — [short topic title]

Status: [1-2 sentences: where things stand right now]

Decisions made:
- [decision] — why: [reason]

Open tasks:
- [ ] [task]

References (don't duplicate content, just point to it):
- [file path / Notion ID / PR link / URL]

Tried and discarded:
- [approach] — why dropped: [reason]

Suggested skills for the next session:
- [skill name] — [when/why it applies here]

Next focus: [only if the user passed $ARGUMENTS — fold their stated focus in here]
```

## Notes

- If the user passed arguments describing what the next session is for, let that shape the whole document — trim sections that aren't relevant to that focus rather than dumping everything.
- Keep it tight. This is meant to load fast in a fresh session, not replace the original conversation.
- If nothing meaningful has happened yet in the conversation (e.g. invoked immediately at the start), say so plainly instead of inventing content.
