class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        r = 0
        ans = 1
        for i in range(26):
            count[i] = 0
        
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) + 1

            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            ans = max(ans, r-l+1)
        
        return ans


