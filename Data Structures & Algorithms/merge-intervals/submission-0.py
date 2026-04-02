class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        linesweep = []
        for start, end in intervals:
            linesweep.append((start, 1))
            linesweep.append((end, -1))
        
        linesweep.sort(key = lambda x: (x[0], -x[1]))

        count = 0
        start = float('inf')
        for val, openClose in linesweep:
            start = min(start, val)
            count += openClose
            if count == 0:
                ans.append([start, val])
                start = float('inf')
        return ans