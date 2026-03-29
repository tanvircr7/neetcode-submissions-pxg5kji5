class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l, r = 0, 0
        ans = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0)+1

            while (r-l+1) - max(count.values()) > k:
                count[s[l]] = count.get(s[l], 0) - 1
                if count[s[l]]<0:
                    count[s[l]] = 0
                
                l += 1
            
            ans = max(ans, r-l+1)
        
        return ans

