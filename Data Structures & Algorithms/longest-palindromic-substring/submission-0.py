class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]
        iteration = 0

        longest = 0
        longestSub = ""

        for r in range(n):
            for c in range(n - iteration):
                if iteration == 0:
                    dp[c][c] = 1
                    if iteration >= longest:
                        longestSub = s[c:c + iteration + 1]
                        longest = iteration
                elif iteration == 1:
                    if s[c] == s[c+1]:
                        dp[c][c + 1] = 1
                        if iteration >= longest:
                            longestSub = s[c:c + iteration + 1]
                            longest = iteration
                    else:
                        dp[c][c + 1] = 0
                else:
                    if s[c] == s[c+iteration] and dp[c + 1][c + iteration - 1] == 1:
                        dp[c][c + iteration] = 1
                        if iteration >= longest:
                            longestSub = s[c:c + iteration + 1]
                            longest = iteration
                    else:
                        dp[c][c + iteration] = 0
            iteration += 1
        return longestSub


            