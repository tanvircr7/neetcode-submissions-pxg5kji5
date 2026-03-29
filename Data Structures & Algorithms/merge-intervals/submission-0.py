class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]

            if start > lastEnd:
                output.append([start,end])
            else:
                newEnd = max(end, lastEnd)
                output[-1][1] = newEnd
        
        return output