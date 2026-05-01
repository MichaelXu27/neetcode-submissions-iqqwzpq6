class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first = cost[0]
        second = cost[1]
        i = 2
        while i < len(cost):
            temp = min(first + cost[i], second + cost[i])
            first = second
            second = temp
            i += 1
        
        return min(second, first)