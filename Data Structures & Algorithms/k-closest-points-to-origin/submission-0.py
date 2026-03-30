class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def sqroot(x,y):
            return math.sqrt(x ** 2 + y ** 2)
        heap = []
        for x, y in points:
            heapq.heappush_max(heap, (sqroot(x,y), [x, y]))
            if len(heap) > k:
                heapq.heappop_max(heap)
        ans = [item[1] for item in heap]
        return ans