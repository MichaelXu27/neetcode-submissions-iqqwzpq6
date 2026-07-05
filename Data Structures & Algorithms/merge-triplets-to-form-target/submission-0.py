class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur = [0, 0, 0]
        t1, t2, t3 = target[0], target[1], target[2]
        for c1, c2, c3 in triplets:
            if c1 > t1 or c2 > t2 or c3 > t3:
                continue
            else:
                cur[0] = max(cur[0], c1)
                cur[1] = max(cur[1], c2)
                cur[2] = max(cur[2], c3)
        return cur == target