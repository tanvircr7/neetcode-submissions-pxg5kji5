class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])

        dis = [[-1]*C for _ in range(R)]
        dis[0][0] = 0
        dirc = [(-1,0), (1,0), (0,1), (0,-1)]
        q = deque()
        q.append((0,0))

        while q:
            r, c = q.popleft()

            for dx,dy in dirc:
                u = r+dx
                v = c+dy
                if min(u,v)>=0 and u<R and v<C and grid[u][v]==0 and (dis[u][v]==-1 or dis[u][v]>1+dis[r][c]):
                    q.append((u,v))
                    dis[u][v] = 1 + dis[r][c]
        
        
        return dis[R-1][C-1]


            





        




            

        