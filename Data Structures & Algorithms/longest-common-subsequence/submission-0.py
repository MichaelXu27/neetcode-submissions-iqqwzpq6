class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1] * (len(text1) + 1) for _ in range(len(text2) + 1)]
        ROWS, COLS = len(text2), len(text1)
        
        def dfs(r, c):
            if r >= ROWS or c >= COLS:
                return 0
            if dp[r + 1][c + 1] != -1:
                return dp[r + 1][c + 1]
            
            if text1[c] == text2[r]:
                dp[r + 1][c + 1] = 1 + dfs(r + 1, c + 1)
            else:
                dp[r + 1][c + 1] = max(dfs(r + 1, c), dfs(r, c + 1))
            return dp[r + 1][c + 1]
        
        return dfs(0, 0)
