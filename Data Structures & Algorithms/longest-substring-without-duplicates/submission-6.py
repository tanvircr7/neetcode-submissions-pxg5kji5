class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        tab = {}
        ans = 0

        for r in range(len(s)):
            tab[s[r]] = tab.get(s[r], 0) + 1

            while tab[s[r]] > 1:
                tab[s[l]] -= 1
                l += 1
            
            ans = max(ans, r-l+1)
        
        return ans




