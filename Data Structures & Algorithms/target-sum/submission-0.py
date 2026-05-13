class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def find(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            
            if (i, total) in dp:
                return dp[(i, total)]
            
            add = find(i + 1, total + nums[i])
            subtract = find(i + 1, total - nums[i])

            dp[(i, total)] = add + subtract
            return dp[(i, total)]
        
        return find(0, 0)