class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) >= 2:
            stone1 = heapq.heappop_max(stones)
            stone2 = heapq.heappop_max(stones)
            smashed = abs(stone1 - stone2)
            
            heapq.heappush_max(stones, smashed)
        return stones[0]