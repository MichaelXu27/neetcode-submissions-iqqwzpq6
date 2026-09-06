class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()
        l, r = 0, k
        for i in range(l, r):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
        ans.append(nums[q[0]])
        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            if l >= q[0]:
                q.popleft()
            ans.append(nums[q[0]])
            r += 1
            l += 1
        return ans