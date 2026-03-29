class Solution {
public:

    vector<int>Nums;
    
    void backtrack(int n, int idx, vector<int>& subset, vector<vector<int>>& res){
        if(idx>=n) {
            res.push_back(subset);
            return;
        }
        subset.push_back(Nums[idx]);
        cout<<"with "<<Nums[idx]<<endl;
        for(int i=0;i<subset.size();i++){
            cout<<subset[i]<<" ";
        } cout<<endl;
        backtrack(n, idx+1, subset, res);
        subset.pop_back();
        cout<<"NOT "<<Nums[idx]<<endl;
        for(int i=0;i<subset.size();i++){
            cout<<subset[i]<<" ";
        } cout<<endl;
        backtrack(n, idx+1, subset, res);

    }


    vector<vector<int>> subsets(vector<int>& nums) {
        Nums = nums;
        vector<vector<int>> res;
        vector<int> subset;
        backtrack(Nums.size(), 0, subset, res);
        return res;
    }
};
