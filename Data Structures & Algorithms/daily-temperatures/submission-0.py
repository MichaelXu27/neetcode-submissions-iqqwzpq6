class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                ptemp, pi = stack.pop()
                ans[pi] =  i - pi
            stack.append([temp, i])
        return ans