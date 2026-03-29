class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPali(s):
            l,r = 0, len(s)-1
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        
        l,r = 0, len(s)-1

        while l<r:

            if s[l]!=s[r]:
                skipL, skipR = s[l+1:r+1], s[l:r]
                if (isPali(skipL) or isPali(skipR)):
                    return True
                else:
                    return False
            
            l+=1
            r-=1
        
        return True
