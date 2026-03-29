class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def helper(grid, r, c, visit):

            if min(r,c)<0 or r==ROWS or c==COLS or grid[r][c]==1 or ((r,c) in visit):
                return 0
            
            if r==ROWS-1 and c==COLS-1:
                return 1
            
            visit.add((r,c))

            cnt = 0

            cnt += helper(grid, r+1, c, visit)
            cnt += helper(grid, r-1, c, visit)
            cnt += helper(grid, r, c+1, visit)
            cnt += helper(grid, r, c-1, visit)

            visit.remove((r,c))

            return cnt



        return helper(grid, 0, 0, set())