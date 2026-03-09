#!/usr/bin/env python3
"""Generate a daily coding practice file.

Picks a random algorithm topic and generates a practice template
with a problem, solution, and notes. Keeps the contribution graph active.
"""

import random
import os
from datetime import datetime, timezone

TOPICS = {
    "two_pointers": [
        ("Two Sum Sorted", "Find two numbers in a sorted array that add up to target"),
        ("Container With Most Water", "Find two lines that form container with most water"),
        ("Remove Duplicates", "Remove duplicates from sorted array in-place"),
        ("Trapping Rain Water", "Calculate trapped rainwater between elevation bars"),
        ("Three Sum", "Find all unique triplets that sum to zero"),
    ],
    "sliding_window": [
        ("Max Subarray Sum K", "Find maximum sum subarray of size k"),
        ("Longest Substring No Repeat", "Longest substring without repeating characters"),
        ("Min Window Substring", "Minimum window containing all characters of pattern"),
        ("Fruit Into Baskets", "Maximum fruits you can pick with two baskets"),
        ("Permutation in String", "Check if s2 contains a permutation of s1"),
    ],
    "binary_search": [
        ("Search Rotated Array", "Search in a rotated sorted array"),
        ("Find Peak Element", "Find a peak element in array"),
        ("Koko Eating Bananas", "Minimum eating speed to finish bananas in h hours"),
        ("Search 2D Matrix", "Search for target in row-column sorted matrix"),
        ("Median Two Sorted", "Find median of two sorted arrays"),
    ],
    "dynamic_programming": [
        ("Climbing Stairs", "Count ways to climb n stairs (1 or 2 steps)"),
        ("Coin Change", "Minimum coins to make amount"),
        ("Longest Increasing Subsequence", "Find length of longest increasing subsequence"),
        ("Edit Distance", "Minimum operations to convert word1 to word2"),
        ("House Robber", "Maximum money robbing non-adjacent houses"),
    ],
    "trees": [
        ("Max Depth Binary Tree", "Find maximum depth of binary tree"),
        ("Validate BST", "Check if binary tree is valid BST"),
        ("Level Order Traversal", "BFS level order traversal of binary tree"),
        ("Lowest Common Ancestor", "Find LCA of two nodes in binary tree"),
        ("Serialize Deserialize Tree", "Serialize and deserialize a binary tree"),
    ],
    "graphs": [
        ("Number of Islands", "Count islands in 2D grid"),
        ("Clone Graph", "Deep clone an undirected graph"),
        ("Course Schedule", "Check if all courses can be finished (cycle detection)"),
        ("Word Ladder", "Shortest transformation sequence from begin to end word"),
        ("Network Delay Time", "Dijkstra shortest path in weighted graph"),
    ],
    "linked_list": [
        ("Reverse Linked List", "Reverse a singly linked list"),
        ("Merge Two Sorted Lists", "Merge two sorted linked lists"),
        ("Detect Cycle", "Detect cycle in linked list (Floyd's)"),
        ("LRU Cache", "Implement LRU cache with O(1) get and put"),
        ("Reorder List", "Reorder list L0→Ln→L1→Ln-1→..."),
    ],
    "stack_queue": [
        ("Valid Parentheses", "Check if brackets are balanced"),
        ("Min Stack", "Stack supporting push, pop, getMin in O(1)"),
        ("Daily Temperatures", "Days until warmer temperature using monotonic stack"),
        ("Evaluate RPN", "Evaluate reverse polish notation expression"),
        ("Sliding Window Maximum", "Maximum in each sliding window of size k"),
    ],
    "greedy": [
        ("Jump Game", "Can you reach the last index?"),
        ("Gas Station", "Find starting gas station for circular route"),
        ("Task Scheduler", "Minimum intervals to finish all tasks with cooldown"),
        ("Merge Intervals", "Merge all overlapping intervals"),
        ("Non Overlapping Intervals", "Min removals to make intervals non-overlapping"),
    ],
    "backtracking": [
        ("Subsets", "Generate all subsets of a set"),
        ("Permutations", "Generate all permutations"),
        ("Combination Sum", "Find combinations that sum to target"),
        ("N Queens", "Place N queens on NxN board"),
        ("Word Search", "Find if word exists in 2D grid"),
    ],
}

SOLUTION_TEMPLATES = {
    "two_pointers": '''def solve(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current = nums[left] + nums[right]
        if current == target:
            return [left, right]
        elif current < target:
            left += 1
        else:
            right -= 1
    return []''',
    "sliding_window": '''def solve(s, k):
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
    return max_len''',
    "binary_search": '''def solve(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1''',
    "dynamic_programming": '''def solve(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]''',
    "trees": '''class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root):
    if not root:
        return 0
    return 1 + max(solve(root.left), solve(root.right))''',
    "graphs": '''from collections import deque

def solve(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                bfs(grid, r, c, rows, cols)
                count += 1
    return count

def bfs(grid, r, c, rows, cols):
    queue = deque([(r, c)])
    grid[r][c] = "0"
    while queue:
        row, col = queue.popleft()
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr, nc = row+dr, col+dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                grid[nr][nc] = "0"
                queue.append((nr, nc))''',
    "linked_list": '''class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev''',
    "stack_queue": '''def solve(s):
    stack = []
    pairs = {")": "(", "}": "{", "]": "["}
    for ch in s:
        if ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return len(stack) == 0''',
    "greedy": '''def solve(intervals):
    intervals.sort(key=lambda x: x[1])
    count = 0
    end = float("-inf")
    for s, e in intervals:
        if s >= end:
            count += 1
            end = e
    return count''',
    "backtracking": '''def solve(nums):
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return result''',
}

NOTES = [
    "Time complexity: O(n), Space: O(1)",
    "Time complexity: O(n log n), Space: O(n)",
    "Time complexity: O(n²), Space: O(n)",
    "Key insight: use hash map for O(1) lookup",
    "Key insight: sort first, then use two pointers",
    "Key insight: use monotonic stack for next greater element",
    "Key insight: BFS for shortest path, DFS for exhaustive search",
    "Key insight: break problem into overlapping subproblems",
    "Key insight: greedy choice property — local optimal = global optimal",
    "Key insight: backtrack when constraint is violated",
    "Edge cases: empty input, single element, all same values",
    "Follow-up: can you solve it in-place with O(1) extra space?",
    "Follow-up: what if the input is a stream?",
    "Related: this pattern appears in many interval/scheduling problems",
    "Optimization: early termination when answer is found",
]


def main():
    now = datetime.now(timezone.utc)
    date_str = now.strftime("%Y-%m-%d")
    day_num = (now - datetime(2026, 1, 1, tzinfo=timezone.utc)).days + 1

    # Pick topic and problem based on date (deterministic per day)
    random.seed(date_str)
    topic = random.choice(list(TOPICS.keys()))
    problem_name, problem_desc = random.choice(TOPICS[topic])
    template = SOLUTION_TEMPLATES[topic]
    notes = random.sample(NOTES, k=random.randint(2, 4))

    # Create solution file
    safe_name = problem_name.lower().replace(" ", "_")
    dir_path = f"solutions/{topic}"
    os.makedirs(dir_path, exist_ok=True)
    file_path = f"{dir_path}/{safe_name}.py"

    content = f'''"""
Day {day_num} — {date_str}
Topic: {topic.replace("_", " ").title()}
Problem: {problem_name}
Description: {problem_desc}
"""


{template}


# --- Notes ---
# {chr(10).join("# " + n for n in notes)}


if __name__ == "__main__":
    # Quick test
    print("Day {day_num}: {problem_name}")
    print("Topic: {topic.replace("_", " ").title()}")
'''

    with open(file_path, "w") as f:
        f.write(content)

    # Update progress log
    log_line = f"| {day_num} | {date_str} | {topic.replace('_', ' ').title()} | {problem_name} |\n"
    log_path = "progress.md"
    if not os.path.exists(log_path):
        with open(log_path, "w") as f:
            f.write("# Daily Coding Practice Log\n\n")
            f.write("| Day | Date | Topic | Problem |\n")
            f.write("|-----|------|-------|---------|\n")

    with open(log_path, "a") as f:
        f.write(log_line)

    print(f"Generated: {file_path}")
    print(f"Day {day_num}: {problem_name} ({topic})")


if __name__ == "__main__":
    main()
