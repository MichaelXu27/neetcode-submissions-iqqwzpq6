class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        dic = Counter(nums)

        for key, value in dic.items():
            heapq.heappush(heap, (value, key))

            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = []
        for key, val in heap:
            ans.append(val)
        return ans
        
            