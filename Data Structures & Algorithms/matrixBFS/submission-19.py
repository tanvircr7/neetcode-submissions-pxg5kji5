class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])

        dis = [[10000]*C for i in range(R)]
        dis[0][0] = 0

        dirc = [(-1,0), (1,0), (0,-1), (0,1)]
        
        q = deque()
        q.append((0,0))

        while q:
            u,v = q.popleft()


            for dx,dy in dirc:
                x = u+dx
                y = v+dy    
                if min(x,y)>=0 and x<R and y<C and grid[x][y]==0 and dis[x][y] > dis[u][v]+1:
                    dis[x][y] = dis[u][v] + 1
                    q.append((x,y))
            
        
        ans = dis[R-1][C-1]
        return ans if ans!=10000 else -1

            





        




            

        