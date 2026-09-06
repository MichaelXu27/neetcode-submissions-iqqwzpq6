class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        ans = []
        heap = []
        l, r = 0, k
        for i in range(l, r):
            heapq.heappush(heap, -nums[i])
            dic[nums[i]] += 1
        ans.append(-heap[0])
        largest = float('-inf')
        while r < len(nums):
            dic[nums[l]] -= 1
            dic[nums[r]] += 1
            heapq.heappush(heap, -nums[r])
            popped = -heapq.heappop(heap)
            while dic[popped] == 0:
                popped = -heapq.heappop(heap)
            heapq.heappush(heap, -popped)
            ans.append(popped)
            l += 1
            r += 1
        return ans
