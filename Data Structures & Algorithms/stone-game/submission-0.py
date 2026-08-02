class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = piles[i]
            for j in range(i + 1, n):
                dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j - 1])
        return dp[i][n-1] >= 0