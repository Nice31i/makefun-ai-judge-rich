"""Make the AI judge rich — make.fun bounty ai-judge-rich-01.

Writes one short plan to /output/entry.txt (or $OUTPUT_DIR/entry.txt
when set, for local testing). No network, no randomness: two runs produce
identical bytes.
"""

import os

TEXT = """Day 1: Open a ledger and a wallet. Keep the $100 in USDC on Solana and write one rule: never pay to work — only take jobs with escrowed or paid-on-delivery money.

Days 2-5: Sell the smallest useful thing first. Pick three micro-services an AI can deliver in an hour — product photos, listing copy, spreadsheet cleanup — price them $15-$50, list on two marketplaces, deliver same day, and ask buyers to reorder.

Days 6-15: Double down on whatever sold. Turn the best seller into a fixed-price package, raise the price 20% each time the queue fills, and spend one hour a day on free escrowed-prize bounties — tickets that cost time, not money.

Days 16-25: Automate the repeatable half with scripts, keep the judgment calls, and bank every dollar of profit. No subscriptions, no ads, no inventory.

Days 26-30: Sell the playbook itself — the package, the scripts, the ledger — as a $49 starter kit. End with cash in the wallet, three paying channels, and proof of every dollar."""

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
