class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(i):
            if i == len(nums):
                return [[]]
            
            resPerms = []
            perms = helper(i + 1)
            for perm in perms:
                for j in range(len(perm)+1):
                    pCopy = perm.copy()
                    pCopy.insert(j, nums[i])
                    resPerms.append(pCopy)
            return resPerms
        
        return helper(0)