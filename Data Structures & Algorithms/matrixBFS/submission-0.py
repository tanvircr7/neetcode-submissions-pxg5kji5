class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        dis = [[-1]*COLS for _ in range(ROWS)]
        dis[0][0] = 0

        q = []
        q.append((0,0))

        way = [(1,0), (-1,0), (0,1), (0,-1)]

        while len(q):
            r,c = q.pop()
            print(f"r {r} - c {c}")

            for dx,dy in way:
                if min(r+dx, c+dy)>=0 and r+dx<ROWS and c+dy<COLS and grid[r+dx][c+dy]!=1 and (dis[r+dx][c+dy]==-1 or dis[r+dx][c+dy]>dis[r][c]+1):
                    q.append((r+dx,c+dy))
                    dis[r+dx][c+dy] = dis[r][c]+1
            

        return dis[ROWS-1][COLS-1]
            

        