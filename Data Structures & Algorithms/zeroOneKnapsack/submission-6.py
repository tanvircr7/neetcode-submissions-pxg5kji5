class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        m, n = len(profit), capacity
        dp = [[-1]*(n+1) for _ in range(m)]
        val =  self.f(0, capacity, dp, profit, weight)
        for i in range(len(dp)):
            print("---")
            for j in range(len(dp[0])):
                print(dp[i][j])
        return val
    
    def f(self, i, c, dp, p, w):
        if i >= len(p) or c==0:
            return 0
        
        if dp[i][c] != -1:
            return dp[i][c]
        
        val = 0
        
        if c-w[i]>=0:
            val = max(val, self.f(i+1, c-w[i], dp, p, w)+p[i])
        
        val = max(val, self.f(i+1, c, dp, p, w))

        dp[i][c] = val
        return val

