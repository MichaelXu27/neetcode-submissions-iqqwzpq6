class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s, f = 0, 0
        while True:
            s = nums[s]
            f = nums[nums[f]]

            if s == f:
                break
        i = 0
        while True:
            s = nums[s]
            i = nums[i]
            if s == i:
                return s