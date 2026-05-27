class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        frontier = {i : -1 for i in range(n)}
        heap = [(0,0, points[0][0], points[0][1])]
        total_cost = 0
        visited = 0

        while heap:
            distance, index, x, y = heapq.heappop(heap)
            if frontier[index] != -1:
                continue
            frontier[index] = distance
            total_cost += distance
            visited += 1
            if visited == n:
                return total_cost
            
            for i, (x1, y1) in enumerate(points):
                if frontier[i] == -1:
                    heapq.heappush(heap, (abs(x1 - x) + abs(y1 - y), i, x1, y1))
        return total_cost
            