class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        x = newInterval[0]
        y = newInterval[1]

        for i, pair in enumerate(intervals):
            u,v = pair
            print(f"{u} - {v}")
            print(f"{x} xy {y}")

            if v < x:
                res.append([u,v])
            elif y < u:
                res.append([x,y])
                return res + intervals[i:]
            else:
                x = min(x,u)
                y = max(y,v)

        
        res.append([x,y])
        
        return res