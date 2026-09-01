class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        func = lambda c: ord(c)-ord('a')
        cnt1 = {}
        cnt2 = {}
        for c in t:
            v = func(c)
            cnt1[v] = cnt1.get(v,0)+1
        
        reslen, res = float("inf"), [-1, -1]
        l=r=0
        have, need = 0, len(cnt1)

        for r in range(len(s)):

            c = s[r]
            v = func(c)
            cnt2[v] = cnt2.get(v,0)+1

            if c in t and cnt1[v]==cnt2[v]:
                have += 1

            while have==need:
                if r-l+1 < reslen:
                    reslen = r-l+1
                    res = [l,r]
                getout = s[l]
                v = func(getout)
                cnt2[v] -= 1
                if getout in t and cnt1[v]==cnt2[v]+1:
                    have -= 1
                l+=1
            
        
        x,y = res

        return s[x:y+1] if reslen != float("inf") else ""

