class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_nums = 0
        for num in nums:
            xor_nums ^= num
        
        missing_nums = 0
        for n in range(len(nums) + 1):
            missing_nums ^= n
        
        return missing_nums ^ xor_nums