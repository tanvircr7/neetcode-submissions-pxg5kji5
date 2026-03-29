class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="" or len(t)>len(s):
            return ""
        
        cT = {}
        for c in t:
            cT[c] = cT.get(c,0)+1
        cS = {}

        have, need = 0, len(cT)
        res, reslen = [-1, -1], float("infinity")
        l=0

        for r in range(len(s)):
            c = s[r]
            cS[c] = cS.get(c,0)+1

            if c in t and cT[c]==cS[c]:
                have += 1

            if have != need: print("NOT MET")

            while have == need:
                print("MET!!==========")
                if (r-l+1) < reslen:
                    reslen = min(r-l+1, reslen)
                    res = [l,r]

                getout = s[l]

                if getout in t and cT[getout] == cS[getout]:
                    have -= 1

                cS[getout] = cS.get(getout, 0)-1
                l+=1
        
        x,y = res

        return s[x: y+1] if reslen!=float("infinity") else ""
