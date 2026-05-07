class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def dfs(i, cur, total):
            if total == target:
                ans.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            total += candidates[i]
            dfs(i + 1, cur, total)
            cur.pop()
            total -= candidates[i]
            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, cur, total)
        dfs(0, [], 0)
        return ans