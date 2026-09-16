class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []

        cur = 1
        for num in nums:
            cur *= num
            prefix.append(cur)
        
        cur = 1
        for i in range(len(nums) - 1, -1, -1):
            cur *= nums[i]
            suffix.append(cur)
        
        suffix = suffix[::-1]

        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(suffix[i+1])
            elif i == len(nums) - 1:
                ans.append(prefix[i-1])
            else:
                ans.append(prefix[i-1] * suffix[i+1])
        return ans



