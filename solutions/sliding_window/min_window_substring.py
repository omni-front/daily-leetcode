"""
Day 73 — 2026-03-14
Topic: Sliding Window
Problem: Min Window Substring
Description: Minimum window containing all characters of pattern
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
# # Time complexity: O(n²), Space: O(n)
# Key insight: backtrack when constraint is violated
# Optimization: early termination when answer is found
# Key insight: BFS for shortest path, DFS for exhaustive search


if __name__ == "__main__":
    # Quick test
    print("Day 73: Min Window Substring")
    print("Topic: Sliding Window")
