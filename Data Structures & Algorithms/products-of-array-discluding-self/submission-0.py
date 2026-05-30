class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        prefix = []
        suffix = []
        n = len(nums)
        total = 1
        for i in range(n):
            total *= nums[i]
            prefix.append(total)

        total = 1
        for i in range(n - 1, -1, -1):
            total *= nums[i]
            suffix.append(total)
        suffix = suffix[::-1]

        for i in range(n):
            total = 1
            if i == 0:
                ans.append(suffix[i+1])
            elif i == n - 1:
                ans.append(prefix[i - 1])
            else:
                ans.append(suffix[i + 1] * prefix[i -1 ])
        return ans
