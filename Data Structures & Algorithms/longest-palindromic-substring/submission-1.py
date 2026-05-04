class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        dp = [[False] * n for _ in range(n)]
        start, best_len = 0, 1

        # length 1 palindromes
        for i in range(n):
            dp[i][i] = True

        # length >= 2
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                    if dp[i][j] and length > best_len:
                        start = i
                        best_len = length
                else:
                    dp[i][j] = False

        return s[start:start + best_len]