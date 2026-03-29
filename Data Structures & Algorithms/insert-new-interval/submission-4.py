class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        x = newInterval[0]
        y = newInterval[1]

        for i in range(len(intervals)):
            
            if y < intervals[i][0]:
                res.append([x,y])
                return res + intervals[i:]
            
            elif x > intervals[i][1]:
                res.append(intervals[i])
            
            else:
                x = min(x, intervals[i][0])
                y = max(y, intervals[i][1])

        
        res.append([x,y])
        return res