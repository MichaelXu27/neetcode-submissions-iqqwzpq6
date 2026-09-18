class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) >= 2:
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)

            finalStone = abs(stone1 - stone2)

            if finalStone > 0:
                heapq.heappush(heap, -finalStone)
            
        if heap:
            return -heap[-1]
        else:
            return 0