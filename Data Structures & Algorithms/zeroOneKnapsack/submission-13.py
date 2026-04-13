class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        M, N = capacity, len(weight)
        dp = [[-1]*(M+1) for _ in range(N)]
        
        return self.kp(0, capacity, profit, weight, dp)
    
    def kp(self, i, c, p, w, dp):
        if c == 0:
            return 0

        if i==len(w):
            return 0
        
        if dp[i][c] != -1:
            return dp[i][c]
        
        res = self.kp(i+1, c, p, w, dp)

        if c-w[i] >= 0:
            res = max(res, self.kp(i+1, c-w[i], p, w, dp) + p[i])

        dp[i][c] = res

        return res



    
