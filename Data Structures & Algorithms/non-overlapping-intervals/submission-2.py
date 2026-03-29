class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda pairs: pairs[0])

        res = []
        res.append(intervals[0])
        
        ans = 0

        for start,end in intervals[1:]:
            lastEnd = res[-1][1]

            if start<lastEnd:
                ans += 1
                res[-1][1] = min(lastEnd, end)
            else:
                res.append([start,end])
        
        return ans
