#!/usr/bin/env python3
"""
Human-like commit scheduler.

Decides whether to commit this run, how many files to generate,
and what commit message to use. Simulates real developer patterns:
- No commits on most weekends
- Skip some weekdays randomly (sick days, busy, etc.)
- Sometimes 2-3 commits on productive days
- Varied commit messages
- Respect holidays
"""

import os
import random
from datetime import datetime, timezone

# Japanese + US holidays 2026 (month, day)
HOLIDAYS = {
    (1, 1), (1, 2), (1, 3),     # New Year
    (1, 13),                      # Coming of Age Day
    (2, 11),                      # National Foundation Day
    (2, 23),                      # Emperor's Birthday
    (3, 20),                      # Vernal Equinox
    (4, 29),                      # Showa Day
    (5, 3), (5, 4), (5, 5),     # Golden Week
    (7, 20),                      # Marine Day
    (8, 11),                      # Mountain Day
    (9, 21),                      # Respect for the Aged Day
    (9, 23),                      # Autumnal Equinox
    (10, 12),                     # Sports Day
    (11, 3),                      # Culture Day
    (11, 23),                     # Labor Thanksgiving
    (12, 25),                     # Christmas
    (12, 31),                     # NYE
}

COMMIT_MESSAGES = [
    "solve {topic} problem",
    "add {problem} solution",
    "practice: {topic}",
    "{problem} — {topic}",
    "daily practice — {topic}",
    "work on {problem}",
    "implement {problem}",
    "{topic}: {problem}",
    "solve {problem}",
    "add {topic} exercise",
    "practice {topic} patterns",
    "wip: {problem}",
    "finish {problem} solution",
    "refactor {problem} approach",
]

TOPICS = [
    "two pointers", "sliding window", "binary search", "dp",
    "trees", "graphs", "linked list", "stack", "greedy",
    "backtracking", "heap", "trie", "union find", "intervals",
]

PROBLEMS = [
    "two sum", "container water", "merge intervals", "coin change",
    "valid parentheses", "number of islands", "reverse linked list",
    "climbing stairs", "subsets", "word search", "lru cache",
    "min stack", "course schedule", "task scheduler",
    "longest substring", "search rotated array", "koko bananas",
]


def main():
    now = datetime.now(timezone.utc)
    weekday = now.weekday()  # 0=Mon, 6=Sun
    month_day = (now.month, now.day)
    hour = now.hour

    # Seed with date + hour for consistency within same trigger
    random.seed(f"{now.strftime('%Y-%m-%d')}-{hour}")

    do_commit = True
    commit_count = 1

    # --- SKIP LOGIC ---

    # Holidays: 90% skip
    if month_day in HOLIDAYS:
        if random.random() < 0.9:
            do_commit = False
            _output(False)
            return

    # Sunday: 95% skip
    if weekday == 6:
        do_commit = False
        _output(False)
        return

    # Saturday: 75% skip (only the 9:30 trigger fires)
    if weekday == 5:
        if random.random() < 0.75:
            do_commit = False
            _output(False)
            return

    # Weekdays: only ONE of the 3 triggers should actually commit
    # Use hour to determine which trigger this is
    if weekday < 5:
        # Pick which trigger "wins" today (deterministic per day)
        day_seed = random.Random(now.strftime('%Y-%m-%d'))
        winning_hour = day_seed.choice([7, 10, 14])

        # Only commit if this is the winning trigger (allow ±1h for cron drift)
        if abs(hour - winning_hour) > 1:
            do_commit = False
            _output(False)
            return

        # Still skip some weekdays (~15% chance)
        if random.random() < 0.15:
            do_commit = False
            _output(False)
            return

    # --- COMMIT COUNT ---
    # Most days: 1-2 commits. Rare marathon days: 10+
    roll = random.random()
    if roll < 0.55:
        commit_count = 1    # 55% — normal day
    elif roll < 0.78:
        commit_count = 2    # 23% — productive day
    elif roll < 0.88:
        commit_count = 3    # 10% — very productive
    elif roll < 0.95:
        commit_count = random.randint(4, 6)   # 7% — deep focus day
    elif roll < 0.99:
        commit_count = random.randint(7, 9)   # 4% — long session
    else:
        commit_count = random.randint(10, 15)  # 1% — marathon hackathon

    # --- COMMIT MESSAGE ---
    topic = random.choice(TOPICS)
    problem = random.choice(PROBLEMS)
    msg_template = random.choice(COMMIT_MESSAGES)
    msg = msg_template.format(topic=topic, problem=problem)

    _output(True, commit_count, msg)


def _output(do_commit, commit_count=0, commit_msg=""):
    out = os.environ.get("GITHUB_OUTPUT", "")
    if out:
        with open(out, "a") as f:
            f.write(f"do_commit={'true' if do_commit else 'false'}\n")
            f.write(f"commit_count={commit_count}\n")
            f.write(f"commit_msg={commit_msg}\n")

    status = "COMMIT" if do_commit else "SKIP"
    print(f"[schedule] {status} | count={commit_count} | msg={commit_msg}")


if __name__ == "__main__":
    main()
