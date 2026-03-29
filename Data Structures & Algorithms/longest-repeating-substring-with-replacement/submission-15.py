class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = {}
        l = 0
        ans = 0
        
        for r in range(len(s)):
            c = s[r]
            cnt[c] = cnt.get(c, 0)+1

            while (r-l+1) - max(cnt.values()) > k:
                v = s[l]
                cnt[v] -= 1
                l += 1
            
            ans = max(ans, r-l+1)
        
        return ans