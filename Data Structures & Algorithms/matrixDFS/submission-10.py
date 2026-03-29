class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])

        def dfs(r,c,visited):

            if min(r,c)<0 or r>=R or c>=C or grid[r][c]==1 or (r,c) in visited:
                return 0
            
            if r==R-1 and c==C-1:
                return 1

            cnt = 0
            visited.add((r,c))
            cnt += dfs(r+1,c,visited)
            cnt += dfs(r-1,c,visited)
            cnt += dfs(r, c+1, visited)
            cnt += dfs(r, c-1, visited)

            visited.remove((r,c))
            return cnt

        return dfs(0,0,set())