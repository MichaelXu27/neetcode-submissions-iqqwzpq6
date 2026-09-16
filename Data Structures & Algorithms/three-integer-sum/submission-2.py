class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        print(nums)

        for i in range(n):
            l = i + 1
            r = n - 1
            if i > 0 and nums[i] == nums[i - 1]: continue
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < n and nums[l - 1] == nums[l]:
                        l += 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1
        return ans
                