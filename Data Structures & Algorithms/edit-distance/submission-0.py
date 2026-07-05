class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i >= m:
                return n - j
            if j >= n:
                return m - i

            total = 0
            if word1[i] == word2[j]:
                total += dfs(i + 1, j + 1)
            else:
                total += 1 + min(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1))
            memo[(i,j)] = total
            return total
        return dfs(0, 0)