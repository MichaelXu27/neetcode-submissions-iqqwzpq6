class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def dfs(i, j):

            if (i, j) in memo:
                return memo[(i,j)]

            if j >= len(t):
                return 1
            elif i >= len(s):
                return 0
            
            
            total = 0
            if s[i] == t[j]:
                total += dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                total += dfs(i + 1, j)
            
            memo[(i,j)] = total
            return memo[(i,j)]
        
        return dfs(0, 0)