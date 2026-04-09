class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="" or len(t)>len(s):
            return ""
        
        cT = {}
        for c in t:
            cT[c] = cT.get(c,0)+1
        
        cS = {}
        residx, reslen = [-1, -1], float("inf")
        have, need = 0, len(cT)

        l=0
        for r in range(len(s)):
            c = s[r]
            cS[c] = cS.get(c,0)+1

            if c in t and cT[c] == cS[c]:
                have += 1
            
            while have == need:
                if r-l+1 < reslen:
                    reslen = r-l+1
                    residx = [l,r]
                
                getout = s[l]
                cS[getout] -= 1
                if getout in t and cS[getout]+1 == cT[getout]:
                    have -= 1
                l+=1
        
        x,y = residx

        return s[x:y+1] if reslen!=float("inf") else ""