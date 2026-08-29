class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = [set() for _ in range(len(nums) + 1)]

        for key, value in counts.items():
            buckets[value].add(key)
        
        ans = []
        for i in range(len(nums), -1, -1):
            if len(ans) == k:
                break
            for num in buckets[i]:
                ans.append(num)
        return ans

