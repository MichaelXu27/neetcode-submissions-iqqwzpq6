class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #min heap
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)
            