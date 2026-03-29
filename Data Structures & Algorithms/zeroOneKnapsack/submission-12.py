class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        M, N = capacity, len(weight)
        dp = [[-1]*(M+1) for _ in range(N)]
        return self.dfs(0,capacity, profit, weight, dp)
    
    def dfs(self, i, curr, p, w, dp):
        if curr==0:
            return 0
            
        if i>=len(profit):
            return 0
        
        if dp[i][curr] != -1:
            return dp[i][curr]
        
        res = self.dfs(i+1, curr, p, w, dp)

        if curr-w[i]>=0:
            res = max(res, self.dfs(i+1, curr-w[i], p, w, dp)+p[i])

        dp[i][curr] = res
        return res
    

    
