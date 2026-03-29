class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        dis = [[-1]*COLS for _ in range(ROWS)]

        dis[0][0] = 0

        dirc = [(-1,0), (1,0), (0,-1), (0,1)]
        q = deque()
        q.append((0,0))

        while len(q):
            u, v = q.popleft()

            for dx, dy in dirc:
                if min(u+dx, v+dy)>=0 and u+dx<ROWS and v+dy<COLS and grid[u+dx][v+dy]==0 and (dis[u+dx][v+dy]==-1 or dis[u+dx][v+dy]>dis[u][v]+1):
                    print('here')
                    q.append((u+dx, v+dy))
                    dis[u+dx][v+dy] = dis[u][v]+1
        
        return dis[ROWS-1][COLS-1]

            

        