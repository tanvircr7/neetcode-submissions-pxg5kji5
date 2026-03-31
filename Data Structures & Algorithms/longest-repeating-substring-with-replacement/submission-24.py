class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = {}
        l = 0
        r = 0

        ans = 0

        while r<len(s):
            c = s[r]
            cnt[c] = cnt.get(c,0)+1

            while (r-l+1) - max(cnt.values()) > k:

                getout = s[l]
                cnt[getout] -= 1
                l += 1
            
            ans = max(ans, r-l+1)

            r+=1
        
        return ans