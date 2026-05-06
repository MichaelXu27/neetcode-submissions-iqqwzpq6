class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]* n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False
                    

        count = 0
        for i in range(n):
            for j in range(n):
                if dp[i][j] == 1:
                    count += 1
        return count

