class Solution:
    def jump(self, nums: List[int]) -> int:
        jump_boundary = 0
        jumps = 0
        distance = 0
        for i in range(len(nums)-1):
            distance = max(distance, i + nums[i])
            if i == jump_boundary:
                jumps += 1
                jump_boundary = distance
        return jumps 