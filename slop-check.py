#!/usr/bin/env python3
"""
slop-check: scan a file for AI writing patterns.

Usage:
    ./slop-check.py <file>
    cat draft.md | ./slop-check.py
"""

import json
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
WORDS_FILE = SCRIPT_DIR / "data" / "slop-words.json"
PHRASES_FILE = SCRIPT_DIR / "data" / "slop-phrases.json"

RED = "\033[0;31m"
YELLOW = "\033[0;33m"
BLUE = "\033[0;34m"
BOLD = "\033[1m"
NC = "\033[0m"


def load_json(path):
    with open(path) as f:
        return json.load(f)


def count_matches(text, pattern):
    return len(re.findall(pattern, text, re.IGNORECASE))


def build_word_pattern(word):
    """Build a regex that matches a word and its common inflections."""
    # Strip parenthetical notes like "(verb)" or "(metaphorical)"
    base = re.sub(r"\s*\(.*?\)\s*", "", word).strip().lower()

    if " " in base:
        # Multi-word: match literally
        return r"\b" + re.escape(base) + r"\b"

    if base.endswith("e"):
        # handle: leverage -> leveraged, leveraging, leverages
        return r"\b" + re.escape(base[:-1]) + r"(?:e|ed|es|ing)\b"
    elif base.endswith("y"):
        # handle: synergy -> synergies
        return r"\b" + re.escape(base) + r"(?:|ies)\b"
    else:
        # handle: delve -> delves, delved, delving
        return r"\b" + re.escape(base) + r"(?:|s|ed|ing|es|d)\b"


def main():
    # Read input
    if len(sys.argv) >= 2 and Path(sys.argv[1]).is_file():
        text = Path(sys.argv[1]).read_text()
        source = sys.argv[1]
    elif not sys.stdin.isatty():
        text = sys.stdin.read()
        source = "stdin"
    else:
        print(f"Usage: {sys.argv[0]} <file>")
        print(f"       cat draft.md | {sys.argv[0]}")
        sys.exit(1)

    # Load patterns from JSON
    words_data = load_json(WORDS_FILE)
    phrases_data = load_json(PHRASES_FILE)

    tier1_hits = 0
    tier2_hits = 0
    filler_hits = 0

    print()
    print(f"{BOLD}ANTI-SLOP SCAN: {source}{NC}")
    print("━" * 50)

    # Tier 1
    print(f"\n{RED}{BOLD}TIER 1 — Kill on sight{NC}")
    for entry in words_data["tier1"]["words"]:
        pattern = build_word_pattern(entry["slop"])
        n = count_matches(text, pattern)
        if n > 0:
            label = entry["slop"]
            print(f"  {RED}{label:<30}{NC} {n} hit(s)")
            tier1_hits += n

    # Tier 2
    print(f"\n{YELLOW}{BOLD}TIER 2 — Suspicious in clusters{NC}")
    for entry in words_data["tier2"]["words"]:
        pattern = build_word_pattern(entry["slop"])
        n = count_matches(text, pattern)
        if n > 0:
            label = entry["slop"]
            print(f"  {YELLOW}{label:<30}{NC} {n} hit(s)")
            tier2_hits += n

    # Filler phrases
    print(f"\n{BLUE}{BOLD}FILLER PHRASES — Delete these{NC}")
    for entry in phrases_data["filler_phrases"]:
        phrase = entry["phrase"]
        pattern = re.escape(phrase)
        n = count_matches(text, pattern)
        if n > 0:
            print(f"  {BLUE}{phrase:<30}{NC} {n} hit(s)")
            filler_hits += n

    # Summary
    total = tier1_hits + tier2_hits + filler_hits
    print()
    print("━" * 50)

    if total == 0:
        print(f"{BOLD}Clean.{NC} No slop detected.")
        sys.exit(0)

    print(
        f"{BOLD}RESULTS:{NC} "
        f"{RED}{tier1_hits} tier-1{NC} | "
        f"{YELLOW}{tier2_hits} tier-2{NC} | "
        f"{BLUE}{filler_hits} filler{NC} | "
        f"{BOLD}{total} total{NC}"
    )

    if tier1_hits > 0:
        print(f"\n{RED}⚠ Tier 1 hits found. Rewrite those sentences.{NC}")
        sys.exit(2)
    elif tier2_hits >= 3:
        print(f"\n{YELLOW}⚠ Multiple tier-2 hits. Check for clustering.{NC}")
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
