"""
Day 80 — 2026-03-21
Topic: Greedy
Problem: Non Overlapping Intervals
Description: Min removals to make intervals non-overlapping
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
# # Optimization: early termination when answer is found
# Key insight: use monotonic stack for next greater element
# Follow-up: can you solve it in-place with O(1) extra space?


if __name__ == "__main__":
    # Quick test
    print("Day 80: Non Overlapping Intervals")
    print("Topic: Greedy")
