class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)< len(t):
            return ""
        
        cnt1 = {}
        for c in t:
            cnt1[c] = cnt1.get(c,0)+1
        cnt2 = {}
        reslen, residx = float("inf"), [-1,-1]
        l=r=0
        have, need = 0, len(cnt1)

        for r in range(len(s)):
            c = s[r]
            cnt2[c] = cnt2.get(c,0)+1

            if c in t and cnt1[c]==cnt2[c]:
                have += 1
            
            while have == need:
                if r-l+1 < reslen:
                    reslen = r-l+1
                    residx = [l,r]
                getout = s[l]
                cnt2[getout]-=1
                if getout in t and cnt1[getout]-1==cnt2[getout]:
                    have -= 1
                l+=1
            
        x,y = residx

        return s[x:y+1] if reslen!=float("inf") else ""

