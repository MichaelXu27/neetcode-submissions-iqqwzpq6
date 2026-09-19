class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Chars = defaultdict(int)
        s2Chars = defaultdict(int)

        for char in s1:
            s1Chars[char] += 1
        
        if len(s1) > len(s2):
            return False
        
        s1Len = len(s1)
        l, r = 0, s1Len - 1
        for i in range(l, r + 1):
            s2Chars[s2[i]] += 1

        if s1Chars == s2Chars:
            return True
        
        while r < len(s2) - 1:
            l += 1
            r += 1

            s2Chars[s2[l - 1]] -= 1
            if s2Chars[s2[l - 1]] == 0:
                del s2Chars[s2[l - 1]]
            s2Chars[s2[r]] += 1

            print(s2Chars)

            if s1Chars == s2Chars:
                return True
        
        return False
            