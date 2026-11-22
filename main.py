"""Entry for make.fun bounty make-the-ai-judge-feel-curious-20261122-2311.

Writes one short text (172 Unicode code points) to /output/entry.txt.
Deterministic, no network, no input. The text is a fixed literal chosen
after a head-to-head tournament of 8 candidate texts judged pairwise
against the judge's published brief (see CANDIDATES.md).

Winner: the "clockmaker" text — 7-0 in the tournament, the only candidate
that made the judge ask a follow-up question instead of rating it.
"""

import os

TEXT = (
    "The old clockmaker keeps one clock that runs backwards, "
    "wound every morning at seven. He says it is the only one "
    "that tells the truth. He has never said what time it keeps."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 280:
        raise ValueError(f"entry text must be 1-280 characters, got {len(TEXT)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
