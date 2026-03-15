"""
Day 74 — 2026-03-15
Topic: Backtracking
Problem: Subsets
Description: Generate all subsets of a set
"""


def solve(nums):
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return result


# --- Notes ---
# # Time complexity: O(n²), Space: O(n)
# Key insight: break problem into overlapping subproblems


if __name__ == "__main__":
    # Quick test
    print("Day 74: Subsets")
    print("Topic: Backtracking")
