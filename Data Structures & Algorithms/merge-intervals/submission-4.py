class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda pair: pair[0])

        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            before = res[-1][1]

            if before < intervals[i][0]:
                res.append(intervals[i])
            else:
                x = min(res[-1][0], intervals[i][0])
                y = max(res[-1][1], intervals[i][1])
                print(f"{x} - {y}")
                res[-1][0] = x
                res[-1][1] = y
        
        return res