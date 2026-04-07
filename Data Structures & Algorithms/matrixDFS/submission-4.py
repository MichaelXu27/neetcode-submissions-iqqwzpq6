class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        if ROWS == 1 and COLS == 1:
            return 1
        ans = 0

        def dfs(r,c):
            nonlocal ans
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 1:
                    continue
                if nr == ROWS - 1 and nc == COLS - 1:
                    ans += 1
                    continue
                grid[nr][nc] = 1
                dfs(nr, nc)
                grid[nr][nc] = 0
        if grid[0][0] == 0:
            grid[0][0] = 1
            dfs(0,0)
        return ans
