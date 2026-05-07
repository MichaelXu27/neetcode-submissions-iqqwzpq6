class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(i, cur, total):
            if total == target:
                ans.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            cur.append(nums[i])
            total += nums[i]
            dfs(i, cur, total)
            cur.pop()
            total -= nums[i]
            dfs(i + 1, cur, total)
        dfs(0, [], 0)
        return ans
