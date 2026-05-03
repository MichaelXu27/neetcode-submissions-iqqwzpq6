class Solution:
    def canJump(self, nums: List[int]) -> bool:
        distance = 0
        for i in range(len(nums)):
            if i > distance:
                return False
            distance = max(distance, i + nums[i])
        return True