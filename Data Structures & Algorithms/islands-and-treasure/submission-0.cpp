class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();

        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(grid[i][j]==0){
                    bfs(i, j, n, m, grid);
                }
            }
        }

        // for(int i=0; i<n; i++){
        //     for(int j=0; j<m; j++){
        //         cout<<grid[i][j]<<" ";
        //     } cout<<endl;
        // }
    }

    void bfs(int i, int j, int n, int m, vector<vector<int>>& grid){
        queue<vector<int>>q;
        q.push({i,j,0});

        while(!q.empty()){
            vector<int> u = q.front();
            q.pop();
            int x = u[0];
            int y = u[1];
            int dis = u[2];

            if(x-1>=0 && grid[x-1][y]!=0 && grid[x-1][y]!=-1 && dis+1<grid[x-1][y]){
                grid[x-1][y] = dis + 1;
                q.push({x-1,y,dis+1});
            }
            if(x+1<n && grid[x+1][y]!=0 && grid[x+1][y]!=-1 && dis+1<grid[x+1][y]){
                grid[x+1][y] = dis + 1;
                q.push({x+1,y,dis+1});
            }
            if(y-1>=0 && grid[x][y-1]!=0 && grid[x][y-1]!=-1 && dis+1<grid[x][y-1]){
                grid[x][y-1] = dis + 1;
                q.push({x,y-1,dis+1});
            }
            if(y+1<m && grid[x][y+1]!=0 && grid[x][y+1]!=-1 && dis<grid[x][y+1]){
                grid[x][y+1] = dis + 1;
                q.push({x,y+1,dis+1});
            }
        }
    }
};
