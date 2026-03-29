class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda pairs: pairs[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = res[-1][1]
            print(lastEnd)

            if start <= lastEnd:
                print("start < = ")
                lastEnd = max(lastEnd, end)
                res[-1][1] = lastEnd
                print(lastEnd)
            else:
                print("input")
                res.append([start,end])
                lastEnd = end
                print(lastEnd)
        
        return res
