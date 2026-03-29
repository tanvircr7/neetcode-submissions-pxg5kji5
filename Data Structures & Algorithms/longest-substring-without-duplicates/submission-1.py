class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charset = set()
        res = 0

        for r in range(len(s)):
            while s[r] in charset:
                # cut of stuff until OK
                charset.discard(s[l])
                l += 1
            charset.add(s[r])
            res = max(res, r-l+1)
        
        return res
