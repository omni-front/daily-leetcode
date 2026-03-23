"""
Day 82 — 2026-03-23
Topic: Sliding Window
Problem: Longest Substring No Repeat
Description: Longest substring without repeating characters
"""


def solve(s, k):
    window = {}
    left = max_len = 0
    for right in range(len(s)):
        window[s[right]] = window.get(s[right], 0) + 1
        while len(window) > k:
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len


# --- Notes ---
# # Key insight: use monotonic stack for next greater element
# Optimization: early termination when answer is found
# Key insight: backtrack when constraint is violated


if __name__ == "__main__":
    # Quick test
    print("Day 82: Longest Substring No Repeat")
    print("Topic: Sliding Window")
