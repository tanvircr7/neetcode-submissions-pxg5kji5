class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        M, N = len(profit), capacity
        dp = [[-1]*(N+1) for _ in range(M)]
        return self.f(0,capacity, dp, profit, weight)
    
    def f(self, i, c, dp, p, w):
        if i>=len(p) or c==0:
            return 0
        
        if dp[i][c]!=-1:
            return dp[i][c]

        res = 0

        if c-w[i]>=0:
            res = max(res, self.f(i+1,c-w[i],dp,p,w)+p[i])
        
        res = max(res, self.f(i+1,c,dp,p,w))

        dp[i][c] = res

        return res

