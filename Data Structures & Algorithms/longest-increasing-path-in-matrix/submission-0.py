class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[-1] * COLS for _ in range(ROWS)] 
        directions = [[1,0], [0,1], [-1,0], [0, -1]]

        def dfs(r, c):
            if dp[r][c] != -1:
                return dp[r][c]
            path = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                    continue
                
                if matrix[r][c] < matrix[nr][nc]:
                    path = max(path, 1 + dfs(nr, nc))
                
            dp[r][c] = path
            return path
        

        longest = 1
        for r in range(ROWS):
            for c in range(COLS):
                longest = max(longest, dfs(r,c))
        return longest