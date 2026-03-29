class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        res = 0
        charset = set()
        while r<len(s):

            while s[r] in charset:
                charset.discard(s[l])
                l += 1
            
            charset.add(s[r])
            
            res = max(res, r-l+1) 
            r += 1
        
        return res
        

