class Solution:
    def longestPalindrome(self, s: str) -> str:
        residx, reslen = -1, 0

        def f(l,r):
            residx, reslen = -1, 0
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1 > reslen:
                    residx = l
                    reslen = r-l+1
                l-=1
                r+=1
            return [residx, reslen]
        
        for i in range(len(s)):
            idx1, len1 = f(i,i)
            idx2, len2 = f(i,i+1)

            idx, length = 0,0
            if len1 < len2:
                idx, length = idx2, len2
            else:
                idx, length = idx1, len1
            
            if reslen<length:
                residx, reslen = idx, length

        return s[residx: residx+reslen]
