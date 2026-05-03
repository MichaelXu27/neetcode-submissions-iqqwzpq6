class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = nums[0]
        maxSum = cur
        for i in range(1, len(nums)):
            if cur < 0 and nums[i] > cur:
                cur = nums[i]
            else:
                cur += nums[i]
            maxSum = max(cur, maxSum)
        return maxSum