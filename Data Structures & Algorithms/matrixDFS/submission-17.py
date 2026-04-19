class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])


        def f(r,c,vis):

            if r<0 or c<0 or r>=R or c>=C or grid[r][c]==1 or (r,c) in vis:
                return 0
            
            if r==R-1 and c==C-1:
                return 1
            
            vis.add((r,c))
            cnt = 0
            cnt += f(r+1, c, vis)
            cnt += f(r-1, c, vis)
            cnt += f(r, c+1, vis)
            cnt += f(r, c-1, vis)
            vis.remove((r,c))

            return cnt
        
        return f(0,0,set())