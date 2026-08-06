class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stk = deque()


        for i, t in enumerate(temperatures):

            while stk and stk[-1][0]<t:
                prev_t, prev_i = stk.pop()
                res[prev_i] = i-prev_i

            stk.append([t, i])



        return res            