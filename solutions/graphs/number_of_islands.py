"""
Day 68 — 2026-03-09
Topic: Graphs
Problem: Number of Islands
Description: Count islands in 2D grid
"""


from collections import deque

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
                queue.append((nr, nc))


# --- Notes ---
# # Key insight: BFS for shortest path, DFS for exhaustive search
# Optimization: early termination when answer is found
# Key insight: use monotonic stack for next greater element
# Key insight: break problem into overlapping subproblems


if __name__ == "__main__":
    # Quick test
    print("Day 68: Number of Islands")
    print("Topic: Graphs")
