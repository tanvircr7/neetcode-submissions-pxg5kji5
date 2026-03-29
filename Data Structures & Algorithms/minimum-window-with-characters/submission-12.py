class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="" or len(t)>len(s):
            return ""
        
        cnt = {}
        for c in t:
            cnt[c] = cnt.get(c,0)+1

        res, reslen = [-1,-1], float("infinity")
        have, need = 0, len(cnt)
        l=0
        cntS = {}
        for r in range(len(s)):
            c = s[r]
            cntS[c] = cntS.get(c,0)+1

            if c in t and cnt[c] == cntS[c]:
                have += 1

            while have == need:
                if r-l+1 < reslen:
                    reslen = r-l+1
                    res = [l,r]
                getthisout = s[l]
                cntS[getthisout] -= 1
                if getthisout in t and cntS[getthisout]+1 == cnt[getthisout]:
                    have -= 1
                l+=1
            
        x,y = res

        return s[x:y+1] if reslen!=float("infinity") else ""