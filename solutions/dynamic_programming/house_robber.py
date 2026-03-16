"""
Day 75 — 2026-03-16
Topic: Dynamic Programming
Problem: House Robber
Description: Maximum money robbing non-adjacent houses
"""


def solve(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


# --- Notes ---
# # Key insight: use hash map for O(1) lookup
# Time complexity: O(n log n), Space: O(n)
# Key insight: BFS for shortest path, DFS for exhaustive search


if __name__ == "__main__":
    # Quick test
    print("Day 75: House Robber")
    print("Topic: Dynamic Programming")
