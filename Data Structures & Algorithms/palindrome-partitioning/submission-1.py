class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(word):
            if len(word) == 1:
                return True
            l, r = 0, len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        ans = []
        path = []
        
        def dfs(i):
            if i >= len(s):
                ans.append(path.copy())
                return
            for j in range(i, len(s)):
                if isPalindrome(s[i: j + 1]):
                    path.append(s[i: j + 1])
                    dfs(j + 1)
                    path.pop()
        dfs(0)
        return ans