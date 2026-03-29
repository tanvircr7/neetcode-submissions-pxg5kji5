class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="" or len(t)>len(s):
            return ""
        
        cntT = {}
        for c in t:
            cntT[c] = cntT.get(c,0)+1
        cntS = {}
        res, reslen = [-1,-1], float("inf")
        have, need = 0, len(cntT)
        l=0
        for r in range(len(s)):
            c = s[r]
            cntS[c] = cntS.get(c,0)+1

            if c in t and cntS[c]==cntT[c]:
                have += 1
            
            while have == need:
                if r-l+1 < reslen:
                    reslen = r-l+1
                    res = [l,r]
                
                getout = s[l]
                cntS[getout] -= 1
                if getout in t and cntS[getout]+1 == cntT[getout]:
                    have -= 1
                l+=1
            
        
        x,y = res

        return s[x:y+1] if reslen!=float("inf") else ""