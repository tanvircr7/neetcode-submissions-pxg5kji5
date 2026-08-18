class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        cnt = 0
        n,m = len(grid), len(grid[0])
        dirc = [(-1,0),(1,0),(0,-1),(0,1)]

        for i in range(n):
            for j in range(m):
                
                if grid[i][j] == 0:
                    continue

                for dx,dy in dirc:
                    u = i+dx
                    v = j+dy

                    if u<0 or u>=n:
                        cnt += 1
                    elif v<0 or v>=m:
                        cnt += 1
                    elif u>=0 and u<n and v>=0 and v<m and grid[u][v]!=1:
                        cnt += 1

        return cnt
                