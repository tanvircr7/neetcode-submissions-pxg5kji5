class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        M, N = len(profit), capacity
        cache = [[-1]*(N+1) for _ in range(M)]
        return self.f(0, profit, weight, capacity, cache)

    def f(self, i, p, w, c, cache):

        if i==len(p):
            return 0
        
        if cache[i][c] != -1:
            return cache[i][c]
        
        x,z = 0,0

        if c-w[i]>=0:
            z = p[i]+self.f(i,p,w,c-w[i], cache)
        y = self.f(i+1, p,w,c, cache)

        val = max(y,z)
        cache[i][c] = val

        return val