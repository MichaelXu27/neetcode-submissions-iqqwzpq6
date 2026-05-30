class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0
        for num in numsSet:
            if num + 1 in numsSet:
                continue
            cur = 1
            temp = num - 1
            while temp in numsSet:
                temp -= 1
                cur += 1
            longest = max(cur, longest)
        return longest