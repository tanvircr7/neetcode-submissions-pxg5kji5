class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        l=0

        ans = 1
        r=0
        cnt = {}
        while r<len(s):
            c = s[r]
            cnt[c] = cnt.get(c,0)+1

            while cnt[c]>1:
                del_c = s[l]
                cnt[del_c] -= 1
                l+=1

            ans = max(ans, r-l+1)
            r+=1
        
        return ans