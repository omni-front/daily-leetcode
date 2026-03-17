"""
Day 76 — 2026-03-17
Topic: Sliding Window
Problem: Fruit Into Baskets
Description: Maximum fruits you can pick with two baskets
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
# # Key insight: break problem into overlapping subproblems
# Key insight: greedy choice property — local optimal = global optimal
# Time complexity: O(n²), Space: O(n)


if __name__ == "__main__":
    # Quick test
    print("Day 76: Fruit Into Baskets")
    print("Topic: Sliding Window")
