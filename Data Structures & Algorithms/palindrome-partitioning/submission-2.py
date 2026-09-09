class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        cur = []

        def isPalindrome(s):
            return s == s[::-1]
        
        def dfs(i):
            if i >= len(s):
                ans.append(cur.copy())
                return 

            for j in range(i, len(s)):
                if isPalindrome(s[i:j + 1]):
                    cur.append(s[i:j+ 1])
                    dfs(j + 1)
                    cur.pop()
        
        dfs(0)
        return ans


            

            
            