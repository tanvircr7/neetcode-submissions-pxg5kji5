class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="" or len(t)>len(s):
            return ""
        cntT = {}
        w = {}
        for c in t:
            cntT[c] = cntT.get(c,0)+1
        
        have, need = 0, len(cntT)
        res, reslen = [-1,-1], float("infinity")
        l, r= 0, 0
        
        for r in range(len(s)):
            c = s[r]
            w[c] = w.get(c,0)+1

            if c in cntT and w[c]==cntT[c]:
                have += 1
            
            while have == need:
                if r-l+1 < reslen:
                    reslen = r-l+1
                    res = [l,r]

                c=s[l]
                if c in cntT and w[c]==cntT[c]:
                    have -= 1
                w[c] = w.get(c,0)-1
                l += 1
            
        l,r = res
        return s[l:r+1] if reslen!=float("infinity") else ""
