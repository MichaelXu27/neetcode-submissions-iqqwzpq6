class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins))]
        
        for r in range(len(dp)):
            dp[r][-1] = 1
        
        for r in range(len(dp) - 1, -1, -1):
            for c in range(len(dp[0]) - 2, -1, -1):
                if c + coins[r] < len(dp[0]):
                    dp[r][c] += dp[r][c + coins[r]]
                if r + 1 < len(coins):
                    dp[r][c] += dp[r + 1][c]


        return dp[0][0]