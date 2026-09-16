class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            if n - 1 in numSet:
                continue
            temp = n
            cur = 0
            while temp in numSet:
                cur += 1
                temp += 1
            longest = max(longest, cur)
        return longest
