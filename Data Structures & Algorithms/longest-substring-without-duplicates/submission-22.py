class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=r=0
        res = 0
        cnt = {}


        for r in range(len(s)):
            c = s[r]
            cnt[c] = cnt.get(c,0)+1

            while cnt[c] > 1:
                getout = s[l]
                cnt[getout] -= 1
                l+=1
            
            res = max(res, r-l+1)
        return res