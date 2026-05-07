class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i == len(nums):
                return 0
            if i in dp:
                return dp[i]
            length = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    length =  max(length, 1 + dfs(j))
            dp[i] = length
            return length
        ans = 1
        for k in range(len(nums)):
            ans = max(ans, dfs(k))
        return ans
