class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="" or len(t)>len(s):
            return ""
        
        cntT = {}
        for c in t:
            cntT[c] = cntT.get(c,0)+1
        

        have, need = 0, len(cntT)
        res, reslen = [-1,-1], float("infinity")

        l=0
        cntS = {}
        for r in range(len(s)):
            c = s[r]
            cntS[c] = cntS.get(c, 0)+1

            if c in t and cntS[c] == cntT[c]:
                have += 1
            
            while have == need:
                if (r-l+1) < reslen:
                    reslen = r-l+1
                    res = [l,r]
                
                v = s[l]
                if cntS[v] == cntT.get(v,0):
                    have -= 1
                cntS[v] -= 1
                l += 1
            
        
        l,r = res

        return s[l:r+1] if reslen < float("infinity") else ""