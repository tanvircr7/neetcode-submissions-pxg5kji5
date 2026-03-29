class Solution {
public:
    vector<vector<int>>adj;
    vector<int>vis;
    vector<int>par;
    bool validTree(int n, vector<vector<int>>& edges) {
        vector<int>v,p;
        vector<vector<int>>list;

        for(int i=0;i<n;i++) {
            v.push_back(0);
            p.push_back(-1);
            list.push_back({});
        }
        vis = v;
        par = p;
        
        for(auto& pair: edges){
            list[pair[0]].push_back(pair[1]);
            list[pair[1]].push_back(pair[0]);
        }
        adj = list;

        for(int i=0;i<vis.size();i++){
            if(vis[i]==0){
                if(dfs(i,-1)){
                    return false;
                }
            }
        }

        int parC=0;
        for(auto& v: par){
            if(v==-1) parC++;
        }

        if(parC>1) return false;

        return true;
    }

    bool dfs(int u, int parent){
        vis[u]=1;
        par[u]=parent;
        for(auto& v: adj[u]){
            if(vis[v]==1 && v!=parent) return true;

            if(vis[v]==0 && v!=parent){
                if(dfs(v, u)){
                    return true;
                }
            }
        }
        return false;
    }
};
