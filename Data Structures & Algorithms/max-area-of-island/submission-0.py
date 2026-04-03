class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            nonlocal count
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0):
                count -= 1
                return
            
            grid[r][c] = 0
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                count += 1
                dfs(nr, nc)
            return count

        ans = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    count = 1
                    ans = max(dfs(r,c), ans)
        return ans