class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])

        dis = [[-1]*C for i in range(R)]

        dis[0][0] = 0

        q = deque()
        q.append([0,0])

        dirc = [(-1,0), (1, 0), (0, -1), (0, 1)]

        while q:
            i,j = q.popleft()

            for dx, dy in dirc:
                u = i+dx
                v = j+dy

                if u>=0 and v>=0 and u<R and v<C and grid[u][v]==0 and (dis[u][v]==-1 or dis[u][v]> 1+dis[i][j]):
                    q.append((u,v))
                    dis[u][v] = 1 + dis[i][j]
        
        return dis[R-1][C-1]




            





        




            

        