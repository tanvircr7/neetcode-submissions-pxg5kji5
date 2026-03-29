class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        idx = len(profit)-1
        return self.f(0, profit, weight, capacity)

    def f(self, i, p, w, c):

        if i==len(p):
            return 0
        
        x,z = 0,0

        if c-w[i]>=0:
            x = p[i]+self.f(i+1, p,w,c-w[i])
            z = p[i]+self.f(i,p,w,c-w[i])
        y = self.f(i+1, p,w,c)

        val = max(x,y,z)

        return val