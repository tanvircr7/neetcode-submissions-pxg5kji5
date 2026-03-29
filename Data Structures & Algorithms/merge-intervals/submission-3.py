class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda pair: pair[0])

        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            end = res[-1][1]
            x = intervals[i][0]
            y = intervals[i][1]
            
            if end >= x:
                res[-1][1] = max(res[-1][1], y)
            else:
                res.append([x,y])
        
        return res