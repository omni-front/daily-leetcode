"""
Day 70 — 2026-03-11
Topic: Trees
Problem: Validate BST
Description: Check if binary tree is valid BST
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root):
    if not root:
        return 0
    return 1 + max(solve(root.left), solve(root.right))


# --- Notes ---
# # Key insight: backtrack when constraint is violated
# Time complexity: O(n), Space: O(1)
# Follow-up: can you solve it in-place with O(1) extra space?


if __name__ == "__main__":
    # Quick test
    print("Day 70: Validate BST")
    print("Topic: Trees")
