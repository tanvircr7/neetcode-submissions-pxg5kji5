class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        M, N = len(profit), capacity
        dp = [[-1]*(N+1) for _ in range(M)]
        return self.dfs(0, capacity, dp, profit, weight)
    
    def dfs(self, i, left, dp, p, w):
        if left == 0:
            return 0
        if i>=len(p):
            return 0
        if dp[i][left] != -1:
            return dp[i][left]
        res = -1
        if left-w[i]>=0:
            res = max(res, p[i]+self.dfs(i+1, left-w[i], dp, p, w))
        res = max(res, self.dfs(i+1, left, dp, p, w))
        dp[i][left] = res
        return res
    
