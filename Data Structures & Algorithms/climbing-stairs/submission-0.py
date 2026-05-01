class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        i = 3
        first = 1
        second = 2
        while i <= n:
            i += 1
            temp = first + second
            first = second
            second = temp
        return second