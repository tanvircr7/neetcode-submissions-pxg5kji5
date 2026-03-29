class Solution {
public:


    int countComponents(int n, vector<vector<int>>& edges) {

        vector<vector<int>>adj(n, vector<int>());
        for(auto edge: edges){
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }

        vector<int>vis(n,0);
        int comp = 0;

        for(int i=0;i<vis.size();i++){
            if(vis[i]==0){
                // cout<<" ----------- "<<endl;
                comp++;

                queue<int>q;
                q.push(i);

                while(!q.empty()){
                    int v = q.front();
                    vis[v] = 1;
                    q.pop();
                    // cout<<"dig "<<v<<endl;

                    for(auto u: adj[v]){
                        if(vis[u]==0){
                            q.push(u);
                        }
                    }
                }
                // cout<<" ----------- "<<endl;

            }
        }
        

        return comp;

    }
};
