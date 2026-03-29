class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        res = self.f(0, profit, weight, capacity)
        return res

    def f(self, i, p, w, c):

        if i>=len(p):
            return 0
        
        val1 = 0
        if c-w[i] >= 0:
            val1 = self.f(i+1, p, w, c-w[i]) + p[i]
        val2 = self.f(i+1, p, w, c)

        return max(val1, val2)