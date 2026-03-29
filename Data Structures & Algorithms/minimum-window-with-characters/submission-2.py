class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s):
            return ""
        
        countT, W = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c,0)
        
        res, reslen = [-1,-1], float("infinity")

        l = 0
        have, need = 0, len(countT)
        for r in range(len(s)):
            c = s[r]
            W[c] = 1 + W.get(c,0)

            if c in countT and W[c]==countT[c]:
                have += 1
            
            while have == need:
                if r-l+1 < reslen:
                    reslen = r-l+1
                    res = [l,r]
                
                W[s[l]] -= 1
                if s[l] in countT and W[s[l]]+1 == countT[s[l]]:
                    have -= 1
                l += 1
    
        l,r = res

        return s[l:r+1] if reslen != float("infinity") else ""