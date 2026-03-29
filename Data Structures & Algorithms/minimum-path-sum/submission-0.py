class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1]*n for _ in range(m)]
        dp[m-1][n-1] = grid[m-1][n-1]

        def f(i,j,dp):
            if (i<0 or i>=m) or (j<0 or j>=n):
                return 10000
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            res = 0

            res = min(f(i+1,j,dp),f(i,j+1,dp))

            print(f"min branch at {i}{j}: {res} + {grid[i][j]}")

            dp[i][j] = res + grid[i][j]
            print(dp)
            return dp[i][j]
        
        ans = f(0,0,dp)
        print(dp)

        return ans