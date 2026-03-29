class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        M, N = len(profit), capacity
        dp = [[-1]*(N+1) for _ in range(M)]
        res = self.f(0, profit, weight, capacity, dp)
        return res

    def f(self, i, p, w, c, dp):

        if i==len(p) or c==0:
            return 0

        if dp[i][c] != -1:
            return dp[i][c]
        
        val1 = 0
        if c-w[i] >= 0:
            val1 = self.f(i+1, p, w, c-w[i], dp) + p[i]
        val2 = self.f(i+1, p, w, c, dp)

        dp[i][c] = max(val1, val2)

        return dp[i][c]