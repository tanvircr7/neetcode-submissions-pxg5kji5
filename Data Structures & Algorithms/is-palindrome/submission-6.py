class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        func = lambda c: ord(c)-ord('a')

        def anum(c: char):
            if func('a')<=func(c)<=func('z') or func('A')<=func(c)<=func('Z') or func('0')<=func(c)<=func('9'):
                return True
            return False
        
        l,r =0, len(s)-1

        while l<r:
            while l<r and anum(s[l])==False:
                l+=1
            while l<r and anum(s[r])==False:
                r-=1
            
            if s[l].lower()!=s[r].lower():
                return False
            
            l+=1
            r-=1
        
        return True



    