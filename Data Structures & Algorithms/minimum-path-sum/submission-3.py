class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dp = [[-1]*(n+1) for _ in range(m+1)]
        dp[m-1][n-1] = grid[m-1][n-1]

        def f(i,j):
            if i<0 or j<0 or i>=m or j>=n:
                return 100000
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            res = min(f(i+1,j), f(i,j+1))

            res += grid[i][j]

            dp[i][j] = res
            return res
        
        return f(0,0)