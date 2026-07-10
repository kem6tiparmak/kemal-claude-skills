#!/usr/bin/env python3
"""Scan a text for em dashes and common AI-writing tells.

Usage:
    python3 check_text.py "<text>"
    python3 check_text.py --file path/to/text.md
    echo "some text" | python3 check_text.py

Em dashes are a hard fail (exit code 1). Flagged vocabulary/phrases are
printed as warnings for human judgment, not treated as automatic errors.
"""

import re
import sys

BANNED_WORDS = [
    "delve", "tapestry", "testament", "pivotal", "underscore", "underscores",
    "foster", "fostering", "boast", "boasts", "vibrant", "crucial", "meticulous",
    "intricate", "interplay", "garner", "garnered", "bolstered", "enduring",
    "showcasing", "robust", "seamless", "realm", "plethora", "groundbreaking",
    "renowned", "nestled", "game-changer", "game-changing",
    "maßgeblich", "vielfältig", "wegweisend", "ganzheitlich", "bahnbrechend",
]

BANNED_PHRASES = [
    "unlock the potential of", "unleash the power of", "embark on",
    "at the forefront of", "harness the power of", "pave the way for",
    "bridging the gap between", "in the realm of",
    "it's important to note that", "it's worth noting that",
    "not just x, it's y",
    "spannende reise", "im bereich von", "auf augenhöhe",
    "es ist wichtig zu betonen, dass", "zusammenfassend lässt sich sagen",
    "industry reports suggest", "some critics argue", "observers have noted",
    "experten zufolge", "manche kritiker argumentieren",
]

EM_DASH = "—"


def scan(text):
    findings = {"em_dashes": [], "words": [], "phrases": []}

    for m in re.finditer(EM_DASH, text):
        start = max(0, m.start() - 30)
        end = min(len(text), m.start() + 30)
        findings["em_dashes"].append(text[start:end].replace("\n", " "))

    lower = text.lower()
    for w in BANNED_WORDS:
        if re.search(r"\b" + re.escape(w.lower()) + r"\b", lower):
            findings["words"].append(w)

    for p in BANNED_PHRASES:
        if p.lower() in lower:
            findings["phrases"].append(p)

    return findings


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--file":
        with open(sys.argv[2], "r", encoding="utf-8") as f:
            text = f.read()
    elif len(sys.argv) > 1:
        text = sys.argv[1]
    else:
        text = sys.stdin.read()

    findings = scan(text)

    exit_code = 0
    if findings["em_dashes"]:
        exit_code = 1
        print(f"FAIL: {len(findings['em_dashes'])} em dash(es) found (hard ban):")
        for ctx in findings["em_dashes"]:
            print(f"  ...{ctx}...")
    else:
        print("OK: no em dashes.")

    if findings["words"]:
        print(f"\nFlagged words ({len(findings['words'])}), review in context:")
        for w in findings["words"]:
            print(f"  - {w}")

    if findings["phrases"]:
        print(f"\nFlagged phrases ({len(findings['phrases'])}), review in context:")
        for p in findings["phrases"]:
            print(f"  - {p}")

    if not findings["words"] and not findings["phrases"]:
        print("\nNo flagged vocabulary/phrases.")

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
