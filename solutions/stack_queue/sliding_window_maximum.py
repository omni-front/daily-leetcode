"""
Day 78 — 2026-03-19
Topic: Stack Queue
Problem: Sliding Window Maximum
Description: Maximum in each sliding window of size k
"""


def solve(s):
    stack = []
    pairs = {")": "(", "}": "{", "]": "["}
    for ch in s:
        if ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return len(stack) == 0


# --- Notes ---
# # Optimization: early termination when answer is found
# Time complexity: O(n log n), Space: O(n)
# Follow-up: what if the input is a stream?


if __name__ == "__main__":
    # Quick test
    print("Day 78: Sliding Window Maximum")
    print("Topic: Stack Queue")
