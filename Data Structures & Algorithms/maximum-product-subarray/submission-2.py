class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]
        minProd = nums[0]
        globalMax = maxProd

        nums = nums[1:]

        for num in nums:
            if num < 0:
                maxProd, minProd = minProd, maxProd
            
            maxProd = max(num, num * maxProd)
            minProd = min(num, num * minProd)

            globalMax = max(globalMax, maxProd)
        return globalMax