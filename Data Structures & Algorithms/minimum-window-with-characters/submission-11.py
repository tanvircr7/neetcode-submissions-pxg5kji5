class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="" or len(t)>len(s):
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

            if c in t and cntT[c]==cntS[c]:
                have += 1
            
            while have == need:
                if r-l+1<reslen:
                    reslen = r-l+1
                    res = [l,r]
                print(f"{l} - {r}")
                v = s[l]
                cntS[v] -= 1
                if v in t and cntT[v]==cntS[v]+1:
                    have -= 1
                l +=1

        l,r = res

        return s[l:r+1] if reslen!=float("infinity") else ""

