"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        currMeetingCnt = ans = 0
        s = e = 0

        while s<len(intervals):

            if start[s] < end[e]:
                currMeetingCnt += 1
                ans = max(ans, currMeetingCnt)
                s += 1
            else:
                currMeetingCnt -= 1
                e += 1
        

        return ans