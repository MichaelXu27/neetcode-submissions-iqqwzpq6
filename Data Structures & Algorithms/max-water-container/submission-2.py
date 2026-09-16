class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n - 1
        most = 0

        while l < r:
            most = max(most, (r - l) * min(heights[l], heights[r]))
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return most
            