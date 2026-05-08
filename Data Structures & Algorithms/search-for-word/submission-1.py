class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c, i, seen):
            
            if i == len(word) - 1 and word[i] == board[r][c]:
                return True
            seen.add((r, c))
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and (nr, nc) not in seen and word[i] == board[r][c]:
                    if dfs(nr, nc, i+1, seen):
                        return True
                    
            seen.remove((r, c))
            return False
        
        ans = False
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    ans = ans or dfs(r, c, 0, set())
        return ans
