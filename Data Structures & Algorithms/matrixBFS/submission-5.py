class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        dis = [[-1]*COLS for _ in range(ROWS)]
        q = deque()
        q.append((0,0))
        dis[0][0] = 0
        dirc = [(-1,0),(1,0),(0,-1),(0,1)]

        while q:
            u,v = q.popleft()

            for dx,dy in dirc:
                x = u+dx
                y = v+dy
                if x>=0 and y>=0 and x<ROWS and y<COLS and grid[x][y]==0 and (dis[x][y]==-1 or dis[x][y]>dis[u][v]+1):
                    q.append((x,y))
                    dis[x][y] = 1+dis[u][v]
        
        return dis[ROWS-1][COLS-1]





        




            

        