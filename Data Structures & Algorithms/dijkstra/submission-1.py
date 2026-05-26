class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjList = {i : [] for i in range(n)}
        print(edges)
        for source, dest, weight in edges:
            adjList[source].append([weight, dest])
        
        shortest = {i: -1 for i in range(n)}
        heap = [(0, src)]
        while heap:
            w, node = heapq.heappop(heap)
            if shortest[node] != -1:
                continue
            else:
                shortest[node] = w

            for nw, node in adjList[node]:
                if shortest[node] == -1:
                    heapq.heappush(heap, (w + nw, node))
        return shortest

        