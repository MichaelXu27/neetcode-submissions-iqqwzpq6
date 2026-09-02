class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        p1, p2 = 0, 0

        dic = defaultdict(int)
        largest = 0
        longest = 0

        while p2 < len(s):
            dic[s[p2]] += 1
            largest = max(dic[s[p2]], largest)
            if p2 - p1 + 1 - largest > k:
                dic[s[p1]] -= 1
                p1 += 1
            longest = max(longest, p2 - p1 + 1)
            p2 += 1
        return longest 
        
        