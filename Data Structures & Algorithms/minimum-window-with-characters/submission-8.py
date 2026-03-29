class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="" or len(t)>len(s):
            return ""
        
        cntT = {}
        for c in t:
            cntT[c] = cntT.get(c,0)+1
        
        cntS = {}
        l=0
        r=0
        res, reslen = [-1,-1], float("infinity")
        have, need = 0, len(cntT)

        while r<len(s):

            c = s[r]
            cntS[c] = cntS.get(c,0)+1

            if c in cntT and cntS[c]==cntT[c]:
                have += 1
            
            while have==need:

                if r-l+1 < reslen:
                    res = [l,r]
                    reslen = r-l+1
                
                cntS[s[l]] -= 1
                if s[l] in cntT and cntS[s[l]]+1 == cntT[s[l]]:
                    have -= 1
                l+=1
            
            r+=1
        
        i,j = res
        return s[i:j+1] if reslen!=float("infinity") else ""



