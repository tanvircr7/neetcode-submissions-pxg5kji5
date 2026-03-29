class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        dis = [[-1]*COLS for _ in range(ROWS)]

        q = deque()
        q.append((0,0))
        dis[0][0] = 0
        dirc = [(0,1), (1,0), (-1,0), (0,-1)]

        while q:
            r,c = q.popleft()

            for dx,dy in dirc:
                u = r+dx
                v = c+dy
                if u>=0 and v>=0 and u<ROWS and v<COLS and grid[u][v]==0 and (dis[u][v]==-1 or (dis[u][v]>dis[r][c]+1)):
                    q.append((u,v))
                    dis[u][v] = dis[r][c]+1



        return dis[ROWS-1][COLS-1]


        





        




            

        