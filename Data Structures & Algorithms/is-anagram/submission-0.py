class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1, s2 = Counter(s), Counter(t)
        return s1 == s2
        