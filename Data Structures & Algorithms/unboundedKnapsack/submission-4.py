class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        M,N = len(profit), capacity
        dp = [[-1]*(N+1) for _ in range(M)]
        return self.kp(0, capacity, dp, profit, weight)
    
    def kp(self, i, leftover, dp, profit, weight):
        if leftover == 0:
            return 0
        
        if i==len(profit):
            return 0
            
        if dp[i][leftover]!=-1:
            return dp[i][leftover]

        res = -1

        if leftover-weight[i]>=0:
            res = max(res, profit[i]+self.kp(i, leftover-weight[i], dp, profit, weight))
        
        res = max(res, self.kp(i+1, leftover, dp, profit, weight))

        dp[i][leftover] = res
        return res