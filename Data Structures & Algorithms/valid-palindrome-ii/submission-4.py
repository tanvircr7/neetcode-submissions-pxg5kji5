class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPali(s: string):
            i,j=0,len(s)-1
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        
        l,r=0,len(s)-1

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