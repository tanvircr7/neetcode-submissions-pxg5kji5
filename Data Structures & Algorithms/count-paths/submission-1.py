class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*n for i in range(m)]
        dp[m-1][n-1] = 1

        def f(i,j):
            if i<0 or i>=m or j<0 or j>=n:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            res = f(i+1,j) + f(i,j+1)
            dp[i][j] = res

            return res
        
        v = f(0,0)

        print(dp)

        return v