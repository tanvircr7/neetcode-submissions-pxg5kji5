class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = {}
        l = r = 0
        res = 0

        for r in range(len(s)):
            c = s[r]
            cnt[c] = cnt.get(c,0)+1

            if (r-l+1) - max(cnt.values()) > k:
                getout = s[l]
                cnt[getout] -= 1
                l+=1
            
            res = max(res, r-l+1)
        
        return res