class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPali(stendal):
            l,r = 0, len(stendal)-1

            while l<r:
                if stendal[l]!=stendal[r]:
                    return False
                else:
                    l+=1
                    r-=1
            
            return True
        

        l,r=0,len(s)-1

        while l<r:

            if s[l]!=s[r]:
                if (isPali(s[l+1:r+1]) or isPali(s[l:r])):
                    return True
                else :
                    return False
            l+=1
            r-=1
        
        return True