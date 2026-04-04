class Solution:
    def islandsAndTreasure(self, rooms: List[List[int]]) -> None:
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(rooms), len(rooms[0])

        def bfs(candidates):
            q = deque()
            for can in candidates:
                q.append(can)

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS:
                        continue
                    if rooms[nr][nc] == 2147483647:
                        rooms[nr][nc] = rooms[r][c] + 1
                        q.append((nr,nc))

        candidates = []
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    candidates.append((r,c))
        bfs(candidates)