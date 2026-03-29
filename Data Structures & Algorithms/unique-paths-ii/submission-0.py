class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[-1]*n for _ in range(m)]
        dp[m-1][n-1] = 1

        def f(i,j,dp):
            if (i<0 or i>=m) or (j<0 or j>=n):
                return 0
            
            if obstacleGrid[i][j] == 1:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            res = 0

            res = f(i+1,j,dp)+f(i,j+1,dp)

            dp[i][j] = res
            return res
        
        ans = f(0,0,dp)
        print(ans)
        return ans