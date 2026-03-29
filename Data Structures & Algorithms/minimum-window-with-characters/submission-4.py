class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="" or len(t)>len(s):
            return ""
       
        cntT = {}
        w = {}

        for c in t:
            cntT[c] = 1 + cntT.get(c,0)
        
        have, need = 0, len(cntT)
        res, reslen = [-1,-1], float("infinity")

        l=0
        for r in range(len(s)):
            c = s[r]
            w[c] = 1 + w.get(c,0)

            if c in cntT and w[c]==cntT[c]:
                have += 1
            
            while have == need:
                if r-l+1 < reslen:
                    reslen = r-l+1
                    res = [l, r]
                
                w[s[l]] -= 1
                if s[l] in cntT and w[s[l]] == cntT[s[l]]-1:
                    have -= 1
                l += 1
        
        l, r = res

        return s[l:r+1] if reslen != float("-infinity") else ""