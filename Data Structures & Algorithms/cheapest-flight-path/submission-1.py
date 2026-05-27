class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = {i: [] for i in range(n)}

        for f, t, p in flights:
            adjList[f].append((t, p))

        print(adjList)
        
        heap = [(0, 0, src)]
        frontier = {i: float('inf') for i in range(n)}
        
        while heap:
            price, planes, cur = heapq.heappop(heap)

            if cur == dst:
                return price

            if planes > k or planes >= frontier[cur]:
                continue
            else:
                frontier[cur] = planes
            
            for connecting, cp in adjList[cur]:
                heapq.heappush(heap, (cp + price, planes + 1, connecting))


        return -1
