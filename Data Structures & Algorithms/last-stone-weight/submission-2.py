class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(heap)
        while len(heap) >= 2:
            y = heapq.heappop_max(heap)
            x = heapq.heappop_max(heap)
            smash = y - x
            if smash != 0:
                heapq.heappush_max(heap, smash)
        return 0 if not heap else heap[0]
