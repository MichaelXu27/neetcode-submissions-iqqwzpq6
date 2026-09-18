class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0
        l, r = 0, 1

        dic = defaultdict(int)
        dic[s[l]] = 1

        ans = 1

        while r < len(s):
            dic[s[r]] += 1
            while dic[s[r]] > 1 and l < r:
                dic[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
            

        return ans
