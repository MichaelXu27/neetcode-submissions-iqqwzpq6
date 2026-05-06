class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP = minP = result = nums[0]

        for num in nums[1:len(nums)]:
            if num < 0:
                maxP, minP = minP, maxP
            
            maxP = max(num, maxP * num)
            minP = min(num, minP * num)

            result = max(result, maxP)
        return result