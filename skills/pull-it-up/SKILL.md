---
name: pull-it-up
description: Use when the user says "pull it up" (or an equivalent request to just show them something) about a program, script, web UI, or piece of content they're meant to actually use or read. Means show the finished, live result on screen — never dump raw file/markdown content into chat, and never ask the user to open it themselves.
---

# Pull It Up

Kemal doesn't want to read source code or raw markdown when he asks to see something — he wants the finished result, already usable, in front of him. Decide the right surface based on what the thing actually is:

| What it is | How to show it |
|---|---|
| Program / script / CLI tool | Run it and open a terminal window that's already executing it and ready for input (e.g. via `osascript`/`Terminal.app`). Do **not** open the source in an editor. |
| Web UI / frontend | Open it rendered in the browser (start the dev server if needed). Do **not** open the source file. |
| Learning material, write-ups, prep docs, anything meant to be read/consumed | Put it in a Google Doc, or write it out directly in the chat reply if it's short. |

## Rules

- Never paste raw `.md` content into the chat as a substitute for doing this properly.
- Never tell Kemal to open the file himself — that defeats the point of asking.
- If you're unsure which category something falls into, default to running/rendering it live rather than showing source — that's the failure mode that has come up before (VS Code with source code did not satisfy a "pull it up" request for a finished program).
