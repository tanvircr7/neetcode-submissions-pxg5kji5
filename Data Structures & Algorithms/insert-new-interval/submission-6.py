class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        x = newInterval[0]
        y = newInterval[1]

        for i in range(len(intervals)):
            p = intervals[i]
            if x>p[1]:
                res.append(p)
            elif y<p[0]:
                res.append([x,y])
                for j in range(i, len(intervals)):
                    res.append(intervals[j])
                return res
            else:
                x = min(p[0], x)
                y = max(p[1], y)

        res.append([x,y])
        
        return res
