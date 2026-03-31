class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        func = lambda x: ord(x)-ord('a')
        cnt1 = {i:0 for i in range(26)}
        cnt2 = {i:0 for i in range(26)}
        for c in s1:
            v = func(c)
            cnt1[v] = cnt1.get(v,0)+1
        for i in range(len(s1)):
            v = func(s2[i])
            cnt2[v] = cnt2.get(v,0)+1
        matches = sum(cnt1[i]==cnt2[i] for i in range(26))

        l=0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            v = func(s2[r])
            cnt2[v] =cnt2.get(v,0)+1

            if cnt2[v] == cnt1[v]:
                matches += 1
            elif cnt2[v]-1 == cnt1[v]:
                matches -= 1
            
            v = func(s2[l])
            cnt2[v] -= 1

            if cnt2[v] == cnt1[v]:
                matches += 1
            elif cnt2[v]+1 == cnt1[v]:
                matches -= 1
            l+=1
        
        return matches == 26