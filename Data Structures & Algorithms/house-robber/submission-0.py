class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        def robFunc(house):
            if house >= len(nums):
                return 0
            if dp[house] != -1:
                return dp[house]

            dp[house] = max(robFunc(house + 1), nums[house] + robFunc(house + 2))
            
            return dp[house]
        return robFunc(0)