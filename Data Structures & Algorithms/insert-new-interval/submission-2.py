class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        

        for i in range(len(intervals)):

            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            else:
                start = min(newInterval[0], intervals[i][0])
                end = max(newInterval[1], intervals[i][1])

                newInterval[0] = start
                newInterval[1] = end
        
        res.append(newInterval)
        return res
