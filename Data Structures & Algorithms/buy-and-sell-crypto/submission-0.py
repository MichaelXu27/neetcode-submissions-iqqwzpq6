class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit = 0
        b = prices[0]

        for s in prices[1:]:
            if s > b:
                bestProfit = max(bestProfit, s - b)
            else:
                b = s
        return bestProfit