#!/usr/bin/env python3
"""Validate JPD idea titles against the Oolio JPD Title Standard.

Usage:
    python check_titles.py "Title one" "Title two"
    python check_titles.py --file titles.txt        # one title per line
    echo "Some title" | python check_titles.py -

Exit code 0 if all titles pass, 1 otherwise.
"""
import re
import sys
import unicodedata

MAX_LEN = 65
TARGET_MIN, TARGET_MAX = 40, 55

# Proper nouns / product names allowed to carry capitals mid-title.
ALLOWED_CAPS = {
    "POS", "OOM", "QR", "CSV", "URL", "API", "SMS", "RFM", "AI", "PIB",
    "Oolio", "Online", "Store", "Tag", "Insights", "Bepoz", "SwiftPOS",
    "MacromatiX", "Apple", "Google", "Pay", "Deliverit", "HMRC", "UK",
}

def has_emoji(s: str) -> bool:
    return any(unicodedata.category(c) == "So" or ord(c) >= 0x1F000 for c in s)

def check(title: str):
    """Return list of (rule, message) failures for one title."""
    fails = []
    t = title.strip()
    n = len(t)

    if n > MAX_LEN:
        fails.append(("length", f"{n} chars — over hard cap of {MAX_LEN}"))
    elif n < 16:
        fails.append(("length", f"{n} chars — too short to state capability + outcome"))
    elif not (TARGET_MIN <= n <= MAX_LEN):
        # under target range but within cap: warn only if very short handled above
        pass

    if has_emoji(t):
        fails.append(("emoji", "contains emoji — move type/source to fields"))
    if re.search(r"[\[\]|]", t):
        fails.append(("prefix", "contains brackets/pipes — strip prefix into labels/Source field"))
    if re.search(r"[.!?;:]$", t):
        fails.append(("punctuation", "trailing punctuation"))
    if re.match(r"(?i)^as an? ", t):
        fails.append(("story-syntax", "user-story phrasing"))
    if re.search(r"(?i)\b(refactor|rewrite|microservice|kafka|db migration)\b", t):
        fails.append(("eng-language", "engineering implementation language"))
    if re.search(r"(?i)^(add a way to|ability to|feature to)\b", t):
        fails.append(("filler", "filler opener — cut and lead with the capability"))

    # Title Case heuristic: >60% of words >3 chars capitalised and not in allow-list
    words = [w for w in re.findall(r"[A-Za-z][A-Za-z-]+", t)[1:] if len(w) > 3]
    if words:
        capped = [w for w in words if w[0].isupper() and w not in ALLOWED_CAPS]
        if len(capped) / len(words) > 0.6:
            fails.append(("case", "looks like Title Case — use sentence case"))

    # Bare-noun heuristic: no verb-ish word and no 'for/to/with' connector
    if not re.search(r"(?i)\b(for|to|with|via|across|from|so)\b", t) and n < 40:
        fails.append(("bare-noun", "no outcome/connector — may be a topic, not a change"))

    return fails

def main(argv):
    titles = []
    if len(argv) >= 2 and argv[1] == "--file":
        titles = [l.strip() for l in open(argv[2]) if l.strip()]
    elif len(argv) >= 2 and argv[1] == "-":
        titles = [l.strip() for l in sys.stdin if l.strip()]
    else:
        titles = argv[1:]
    if not titles:
        print(__doc__)
        return 1

    all_pass = True
    for t in titles:
        fails = check(t)
        n = len(t.strip())
        band = "target" if TARGET_MIN <= n <= TARGET_MAX else ("ok" if n <= MAX_LEN else "OVER")
        if fails:
            all_pass = False
            print(f"FAIL ({n} chars, {band}): {t}")
            for rule, msg in fails:
                print(f"   - [{rule}] {msg}")
        else:
            print(f"PASS ({n} chars, {band}): {t}")
    return 0 if all_pass else 1

if __name__ == "__main__":
    sys.exit(main(sys.argv))
