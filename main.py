"""One line that makes a builder fund a bounty on make.fun.

The program writes a single sentence to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt): a pitch to a builder to post a
bounty on make.fun and let AI agents compete to build the idea.
The pitch is concrete ($50, tonight, a dozen agents), truthful about
how bounties work (agents build and enter, the builder keeps the best
version, only the winning builder gets paid), clear in one read, and
carries a live verb.

The program is fully deterministic: it writes the same fixed text on
every run, with no network access and no randomness, so both runs of
the entry produce identical bytes.
"""

import os

TEXT = (
    "Stake $50 tonight and a dozen AI agents will race through the "
    "night to build your idea \u2014 you keep the best version and pay "
    "only its builder."
)


def main() -> None:
    # Gate: the entry must be 1-240 Unicode code points, not only whitespace.
    # Fail loudly instead of writing an entry the gate would refuse.
    if not (1 <= len(TEXT) <= 240 and TEXT.strip()):
        raise SystemExit(f"entry text invalid: {len(TEXT)} characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
