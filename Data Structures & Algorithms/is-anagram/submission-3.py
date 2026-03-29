class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cntS = {i:0 for i in range(26)}
        f = lambda c: ord(c)-ord('a')

        for c in s:
            cntS[f(c)] += 1
        for c in t:
            cntS[f(c)] -= 1
        
        for i in range(26):
            if cntS[i] != 0:
                return False
        
        return True
