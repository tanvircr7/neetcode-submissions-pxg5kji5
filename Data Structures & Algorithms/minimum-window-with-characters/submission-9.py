class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="" or len(t)>len(s):
            return ""

        cntT = {}
        for c in t:
            cntT[c] = cntT.get(c,0)+1


        res, reslen = [-1,-1], float("infinity")
        have, need = 0, len(cntT)
        l=0
        cntS = {}
        for r in range(len(s)):
            c = s[r]
            cntS[c] = cntS.get(c,0)+1

            if c in t and cntS[c]==cntT[c]:
                have +=1 
            
            while have == need:
                if r-l+1 < reslen:
                    reslen = r-l+1
                    res = [l,r]

                del_c = s[l]
                if del_c in t and cntS[del_c]==cntT[del_c]:
                    have -= 1
                cntS[del_c] -= 1
                l+=1
        
        i,j = res

        return s[i:j+1] if reslen!=float("infinity") else ""




