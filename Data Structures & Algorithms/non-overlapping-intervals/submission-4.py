class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        cnt = 0
        intervals.sort(key = lambda p : p[0])

        res = []
        res.append(intervals[0])
        
        for i in range(1, len(intervals)):
            end = res[-1][1]

            if intervals[i][0] < end:
                y = min(res[-1][1], intervals[i][1])
                res[-1][1] = y
                cnt += 1
            else:
                res.append(intervals[i])
                
        return cnt