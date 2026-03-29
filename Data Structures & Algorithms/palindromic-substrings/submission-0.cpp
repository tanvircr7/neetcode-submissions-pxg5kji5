class Solution {
public:
    int countSubstrings(string s) {
        int ans = 0, cnt = 0;
        string p;

        for(int i=0;i<s.size();i++){
            int l = i;
            int r = i;
            while(l>=0 && r<s.size() && s[l]==s[r]){
                if(r-l+1 > ans){
                    ans = r - l + 1;
                    p = s.substr(l, r-l+1);
                }
                r++;
                l--;
                cnt++;
            }

            l = i;
            r = i+1;
            while(l>=0 && r<s.size() && s[l]==s[r]){
                if(r-l+1 > ans){
                    ans = r - l + 1;
                    p = s.substr(l, r-l+1);
                }
                r++;
                l--;
                cnt++;
            }
        }

        return cnt;
    }
};
