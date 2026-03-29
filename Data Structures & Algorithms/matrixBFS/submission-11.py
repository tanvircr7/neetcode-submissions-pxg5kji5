class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])

        dis = [[-1]*C for i in range(R)]
        q = deque()
        q.append((0,0))
        dis[0][0] = 0
        dirc = [(-1,0), (1,0), (0,-1), (0,1)]

        while q:
            r,c = q.popleft()

            for dx,dy in dirc:
                u = r+dx
                v = c+dy

                if u>=0 and v>=0 and u<R and v<C and (grid[u][v]!=1) and (dis[u][v]==-1 or dis[u][v]> dis[r][c]+1):
                    q.append((u,v))
                    dis[u][v] = dis[r][c]+1
        

        return dis[R-1][C-1]

            





        




            

        