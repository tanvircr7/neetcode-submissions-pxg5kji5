class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        vector<bool> dp(s.size()+1, false);
        dp[s.size()] = true;

        for(int i=s.size()-1; i>=0; i--){
            cout<<"-------i "<<i<<endl;
            for(const auto& w: wordDict){
                cout<<"<<<< w "<<w<<endl;
                if(
                    (i+w.size()) <= s.size() 
                    && 
                    s.substr(i, w.size())==w
                ){
                    cout<<"dp "<<i<<" = "<<dp[i+w.size()]<<endl;
                    dp[i] = dp[i+w.size()];
                }
                if(dp[i]){
                    cout<<"break at "<<i<<endl;
                    break;
                }
            }
        }
        return dp[0];
        
    }
};
