class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dp = [[-1]*n for _ in range(m)]
        dp[m-1][n-1] = grid[m-1][n-1]

        def dfs(i,j):
            if i>=m or i<0 or j>=n or j<0:
                return 10000
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            res = 0
            res = min(dfs(i+1,j), dfs(i,j+1))
            dp[i][j] = res+grid[i][j]

            return dp[i][j]
        
        ans = dfs(0,0)
        print(dp)
        return ans