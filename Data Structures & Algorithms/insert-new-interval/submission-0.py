class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            ans.append([intervals[i][0], intervals[i][1]])
            i += 1
        
        start = newInterval[0]
        end = newInterval[1]

        while i < n and intervals[i][0] <= newInterval[1]:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1

        ans.append([start, end])
        
        while i < n:
            ans.append([intervals[i][0], intervals[i][1]])
            i += 1
        
        return ans