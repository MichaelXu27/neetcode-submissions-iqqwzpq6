class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {i: [] for i in range(1, n + 1)}

        for s, d, w in times:
            adjList[s].append((w, d))
        
        print(adjList)

        heap = [(0, k)]
        frontier = {i: -1 for i in range(1, n + 1)}

        while heap:
            pw, pn = heapq.heappop(heap)
            if frontier[pn] != -1:
                continue
            else:
                frontier[pn] = pw
            
            for nw, nn in adjList[pn]:
                if frontier[nn] == -1:
                    heapq.heappush(heap, (nw + pw, nn))
                    
        
        weights = frontier.values()
        # print(weights)
        if -1 in weights:
            return -1
        else:
            return max(weights)

             
