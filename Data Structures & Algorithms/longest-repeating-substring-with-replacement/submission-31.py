class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=r=0
        res = 0
        cnt = {}

        for r in range(len(s)):
            v = s[r]
            cnt[v] = cnt.get(v,0)+1

            while (r-l+1) - max(cnt.values()) > k:
                getout = s[l]
                cnt[getout] -=1
                l+=1

            res = max(res, r-l+1)
            
        return res