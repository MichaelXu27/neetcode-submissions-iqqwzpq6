class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        cur = []
        def generate(o, c):
            if o == c == n:
                ans.append(''.join(cur.copy()))
                return
            if o < n:
                cur.append('(')
                generate(o + 1, c)
                cur.pop()
            if c < o:
                cur.append(')')
                generate(o, c + 1)
                cur.pop()
        generate(0, 0)
        return ans
                