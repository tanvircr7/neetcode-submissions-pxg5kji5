class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        val = 0
        for i in range(len(intervals)):

            if newInterval[1]<intervals[i][0]:
                res.append(newInterval)
                return res+intervals[i:]
            elif newInterval[0]>intervals[i][1]:
                res.append(intervals[i])
            else:
                x = min(newInterval[0], intervals[i][0])
                y = max(newInterval[1], intervals[i][1])

                newInterval = [x,y]
        
        res.append(newInterval)
        return res
        