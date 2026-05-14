class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            if buying:
                res = max(dfs(i + 1, False) - prices[i], dfs(i + 1, True))


            if not buying:
                res = max(dfs(i + 2, True) + prices[i], dfs(i + 1, False))


            dp[(i, buying)] = res
            return dp[(i, buying)]
        return dfs(0, True)