class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(grid, r, c, visited: set):
            if min(r,c)<0 or r==ROWS or c==COLS or grid[r][c]==1 or (grid[r][c]==0 and (r,c) in visited):
                return 0
            
            if r==ROWS-1 and c==COLS-1:
                return 1
            
            visited.add((r,c))

            cnt = 0
            cnt += dfs(grid, r+1, c, visited)
            cnt += dfs(grid, r-1, c, visited)
            cnt += dfs(grid, r, c+1, visited)
            cnt += dfs(grid, r, c-1, visited)

            visited.remove((r,c))

            return cnt
        
        return dfs(grid, 0, 0, set())