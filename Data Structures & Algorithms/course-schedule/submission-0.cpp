class Solution {
public:
    unordered_map<int, vector<int>> pre;
    vector<int>vis, pathvis;

    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vis.resize(numCourses, 0);
        pathvis.resize(numCourses, 0);

        for(int i=0;i<numCourses;i++) pre[i] = {};

        for(int i=0;i<prerequisites.size();i++){
            pre[prerequisites[i][1]].push_back(prerequisites[i][0]);
        }

        for(int i=0;i<vis.size();i++){
            if(vis[i]==0){
                if(dfs(i)) return false;
            }
        }

        return true;
    }

    bool dfs(int c){
        cout<<"----DFS "<<c<<endl;
        vis[c]=1;
        pathvis[c]=1;
        for(auto& v: pre[c]){
            if(!vis[v]){
                if(dfs(v)) return true;
            }
            else if(vis[v] && pathvis[v]){
                return true;
            }
        }
        pathvis[c]=0;
        return false;
    }
};
