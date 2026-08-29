class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.limit = k
        self.data = nums
        heapq.heapify(self.data)

        while len(self.data) > self.limit:
            heapq.heappop(self.data)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.data, val)

        if len(self.data) > self.limit:
            heapq.heappop(self.data)
        
        return self.data[0]