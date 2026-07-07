#!/usr/bin/env bash
# Sends a prompt (via stdin) to a local Ollama model via its REST API
# and prints the plain-text response.
#
# Usage: delegate.sh [model] < prompt.txt
#        echo "prompt" | delegate.sh
#
# Uses the HTTP API instead of `ollama run` because the CLI emits ANSI
# cursor/spinner control codes that pollute stdout when not attached to
# a real foreground terminal (e.g. when backgrounded). The API returns
# clean JSON with no terminal-formatting side effects.
set -uo pipefail

MODEL="${1:-qwen2.5-coder:7b}"
TIMEOUT="${DELEGATE_TIMEOUT:-60}"
HOST="${OLLAMA_HOST:-127.0.0.1:11434}"

for bin in curl jq; do
  if ! command -v "$bin" >/dev/null 2>&1; then
    echo "Error: $bin is not installed or not on PATH" >&2
    exit 1
  fi
done

prompt="$(cat)"

payload="$(jq -n --arg model "$MODEL" --arg prompt "$prompt" \
  '{model: $model, prompt: $prompt, stream: false}')"

response="$(curl -s --max-time "$TIMEOUT" "http://${HOST}/api/generate" -d "$payload")"

if [ -z "$response" ]; then
  echo "Error: no response from Ollama at ${HOST} (is \`ollama serve\` running?)" >&2
  exit 1
fi

if ! echo "$response" | jq -e '.response' >/dev/null 2>&1; then
  echo "Error: unexpected Ollama response: $response" >&2
  exit 1
fi

echo "$response" | jq -r '.response'
