class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda pair: pair[0])
        res = 0
        curr = [intervals[0]]

        for start, end in intervals[1:]:

            if start < curr[-1][1]:
                print("start < ")
                res += 1
                curr[-1][1] = min(curr[-1][1], end)
                print(res)
            else:
                curr.append([start,end])
                print("append")

        return res
        