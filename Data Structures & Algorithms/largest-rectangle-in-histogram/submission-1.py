class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        ans = 0
        for i, num in enumerate(heights):
            while stack and (heights[stack[-1]] >= num or i == len(heights)):
                popped = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                height = heights[popped]
                ans = max(ans, width * height)
            stack.append(i)
        return ans
