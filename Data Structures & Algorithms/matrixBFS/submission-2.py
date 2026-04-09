class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        def bfs(r,c):
            q = deque()
            q.append((r, c))
            grid[r][c] = 1
            depth = 0
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS:
                            continue
                        if grid[nr][nc] == 1:
                            continue
                        grid[nr][nc] = 1
                        if nr == ROWS - 1 and nc == COLS -1:
                            return depth + 1
                        q.append((nr, nc))
                depth += 1
            return -1

    
        if grid[0][0] == 1:
            return -1
        if 0 == ROWS - 1 and 0 == COLS - 1:
            return 0
        return bfs(0,0)

                
                    