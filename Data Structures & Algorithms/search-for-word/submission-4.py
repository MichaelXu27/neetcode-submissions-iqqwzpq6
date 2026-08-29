class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i, seen):
            if i >= len(word):
                return True
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != word[i] or (r,c) in seen:
                return False
            
            seen.add((r,c))

            up = dfs(r - 1, c, i + 1, seen)
            down = dfs(r + 1, c, i + 1, seen)
            left = dfs(r, c - 1, i + 1, seen)
            right = dfs(r, c + 1, i + 1, seen)

            seen.remove((r, c))

            if up or down or left or right:
                return True
            else:
                return False
            
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0, set()):
                        return True
        return False
