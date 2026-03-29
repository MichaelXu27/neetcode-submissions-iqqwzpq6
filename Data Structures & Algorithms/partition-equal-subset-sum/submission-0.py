class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        half = total // 2
        if half * 2 != total:
            return False
        cache = {}
        def recurse(index, cur):
            if (index, cur) in cache:
                return cache[(index,cur)]
            if cur > half:
                return False
            elif cur == half:
                return True
            elif index < len(nums):
                include = recurse(index + 1, cur + nums[index])
                exclude = recurse(index + 1, cur)
            else:
                return False
            cache[(index, cur)] = include or exclude
            return cache[(index, cur)] 
        return recurse(0, 0)
    