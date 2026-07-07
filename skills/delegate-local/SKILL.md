---
name: delegate-local
description: Delegate well-specified, self-contained writing/coding subtasks to a local Ollama model to save Claude usage. Use automatically (no need to ask first) when a task fits the criteria below, then review the output before integrating it. Not for architecture decisions, security-sensitive code, or ambiguous specs.
---

# Delegate to Local Model

Kemal runs a local Ollama model (`qwen2.5-coder:7b`, 32K context) for offloading
work that doesn't need Claude-level reasoning. The goal is saving Claude usage,
not saving effort — always review the output before it touches a real file.

## When to delegate (decide yourself, don't ask first)

Delegate when the task is:
- Boilerplate or repetitive code (CRUD patterns, simple config, test scaffolding)
- Documentation or comments for already-written code
- A small, self-contained function/component with a clear, unambiguous spec

Do NOT delegate:
- Architecture or design decisions
- Security-sensitive code (auth, payments, secrets, anything touching user data)
- Anything with an ambiguous spec, or that needs iterative debugging —
  a 7B model is weak at multi-step reasoning and will thrash

## How to delegate

1. Write a self-contained prompt: relevant conventions, exact signature/spec,
   and an explicit instruction for output format (e.g. "return only the code,
   no explanation").
2. Run the helper script via Bash, piping the prompt through stdin:
   ```bash
   echo "$PROMPT" | ~/.claude/skills/delegate-local/delegate.sh
   ```
   Optional: pass a different model as `$1`, override timeout via
   `DELEGATE_TIMEOUT` (default 60s).
3. Read the output. Verify it: check syntax, run the project's lint/build/test
   command if one exists, confirm it matches conventions.
4. If good: integrate it yourself via Write/Edit. Briefly note to Kemal that
   this part was locally delegated (transparency, not a formality — he should
   know when code wasn't Claude-reviewed from scratch).
5. If bad: one retry with a more precise prompt, or just write it yourself.
   Don't loop more than once — that defeats the point of saving usage.

## Failure modes

- Ollama not running or model missing → the script exits non-zero with a
  clear error on stderr. Fall back to doing the work yourself and mention it.
- The script uses Ollama's REST API (not `ollama run`), because the CLI
  emits ANSI cursor/spinner codes that corrupt captured output when not
  attached to a real foreground terminal.
