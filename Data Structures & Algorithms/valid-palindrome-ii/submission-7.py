class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPali(st):
            l,r = 0, len(st)-1
            while l<r:
                if st[l]!=st[r]:
                    return False
                l+=1
                r-=1
            return True
        
        l,r = 0, len(s)-1
        while l<r:
            if s[l]!=s[r]:
                if isPali(s[l:r])==False and isPali(s[l+1:r+1])==False:
                    return False
            l+=1
            r-=1
        
        return True