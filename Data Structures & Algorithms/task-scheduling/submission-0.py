class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        counts = Counter(tasks)
        
        for value in counts.values():
            heapq.heappush_max(heap, value)

        q = deque()        

        time = 0
        while heap or q:
            popped = 0
            if heap:
                freq = heapq.heappop_max(heap)
                freq -= 1
                if freq != 0:
                    q.append((freq, n + time))
            
            if q and q[0][1] == time:
                cnt, _ = q.popleft()
                heapq.heappush_max(heap, cnt)

            
            time += 1
        return time


