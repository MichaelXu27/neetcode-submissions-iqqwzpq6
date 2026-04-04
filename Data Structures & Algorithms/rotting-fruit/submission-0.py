class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(candidates):
            nonlocal time
            q = deque()
            for can in candidates:
                q.append(can)
            
            while q:
                n = len(q)
                for _ in range(n):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS:
                            continue
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            q.append((nr, nc))
                time += 1

        candidates = []
        time = -1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    candidates.append((r,c))
        bfs(candidates)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2 or grid[r][c] == 0:
                    continue
                else:
                    return -1
        
        return 0 if time == -1 else time

