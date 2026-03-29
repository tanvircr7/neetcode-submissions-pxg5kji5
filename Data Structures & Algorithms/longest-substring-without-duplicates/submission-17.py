class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        
        l=0
        reslen=1
        cnt = {}
        for r in range(len(s)):
            c = s[r]
            cnt[c] = cnt.get(c,0)+1

            while cnt[c] > 1:
                getthisout = s[l]
                cnt[getthisout] -= 1
                l+=1
            
            reslen = max(reslen, r-l+1)
        
        return reslen
