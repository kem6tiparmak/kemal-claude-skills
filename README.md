# Claude Code Skills

A collection of custom [Claude Code](https://claude.com/claude-code) skills I designed and use in my own workflow.

Skills are reusable, self-contained instructions that extend what Claude Code can do — think of them as small plugins triggered by a slash command or by matching a description. Each skill lives in its own folder with a `SKILL.md` that defines when and how it should run.

## Skills

| Skill | What it does |
|-------|--------------|
| [`handoff`](skills/handoff/SKILL.md) | Generates a structured handoff prompt summarizing the current conversation (decisions made, open tasks, discarded approaches), so it can be pasted into a fresh session. Faster and more targeted than `/compact` because it does one deliberate pass instead of re-summarizing the whole transcript. |
| [`delegate-local`](skills/delegate-local/SKILL.md) | Offloads well-specified, low-stakes coding subtasks (boilerplate, docs, small self-contained functions) to a local Ollama model, to save Claude usage on work that doesn't need Claude-level reasoning. Includes the helper script used to talk to the local model's REST API. |
| [`pull-it-up`](skills/pull-it-up/SKILL.md) | Triggers on "pull it up" — shows the finished, live result of something (a running program, a rendered web UI, a usable document) instead of dumping source code or raw markdown into the chat. |

## Installation

Copy a skill folder into your Claude Code skills directory:

```bash
cp -r skills/handoff ~/.claude/skills/
```

Global skills go in `~/.claude/skills/`; project-scoped skills go in `.claude/skills/` inside a repo.

## About

Built while working on freelance web dev projects and personal SaaS products. Each skill exists because it solved a real, repeated friction point in my own Claude Code workflow.
