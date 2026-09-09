class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        directions = [[0, 1], [1,0], [0, -1], [-1, 0]]
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(i, j):
            q = [(i, j)]
            seen = set()
            seen.add((i, j))
            while q:
                r, c = q.pop()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in seen or grid[nr][nc] == "0":
                        continue
                    seen.add((nr, nc))
                    grid[nr][nc] = "0"
                    q.append((nr, nc))

                    

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands += 1
                    bfs(r, c)
        return islands