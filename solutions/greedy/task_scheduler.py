"""
Day 72 — 2026-03-13
Topic: Greedy
Problem: Task Scheduler
Description: Minimum intervals to finish all tasks with cooldown
"""


def solve(intervals):
    intervals.sort(key=lambda x: x[1])
    count = 0
    end = float("-inf")
    for s, e in intervals:
        if s >= end:
            count += 1
            end = e
    return count


# --- Notes ---
# # Follow-up: what if the input is a stream?
# Key insight: backtrack when constraint is violated
# Optimization: early termination when answer is found


if __name__ == "__main__":
    # Quick test
    print("Day 72: Task Scheduler")
    print("Topic: Greedy")
