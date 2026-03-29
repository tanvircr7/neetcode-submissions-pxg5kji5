class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="" or len(s)<len(t):
            return ""

        cntT = {}
        for c in t:
            cntT[c] = cntT.get(c,0)+1
        
        cntS = {}
        have, need = 0, len(cntT)
        res, reslen = [-1,-1], float("infinity")

        l=0
        for r in range(len(s)):
            c = s[r]
            cntS[c] = cntS.get(c,0)+1

            if c in cntT and cntS[c]==cntT[c]:
                have += 1
            
            while have == need:
                if (r-l+1) < reslen:
                    reslen = r-l+1
                    res = [l,r]
                
                del_c = s[l]
                cntS[del_c] -= 1
                
                if del_c in cntT and cntS[del_c]+1 == cntT[del_c]:
                    have -= 1
                l+=1

        i,j = res

        return s[i:j+1] if reslen<float("infinity") else ""
            


