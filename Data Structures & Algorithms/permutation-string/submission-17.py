class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        func = lambda c: ord(c)-ord('a')
        
        cnt1 = {i:0 for i in range(26)}
        cnt2 = {i:0 for i in range(26)}
        for c in s1:
            cnt1[func(c)] = cnt1.get(func(c),0)+1
        for i in range(len(s1)):
            v = func(s2[i])
            cnt2[v] = cnt2.get(v,0)+1
        matches = sum(cnt1[i]==cnt2[i] for i in range(26))
        l=0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                break
            print(matches)

            c = func(s2[r])
            cnt2[c] = cnt2.get(c,0)+1
            
            if cnt1[c] == cnt2[c]:
                matches += 1
            elif cnt1[c] == cnt2[c]-1:
                matches -= 1
            
            v=func(s2[l])
            cnt2[v] -= 1

            if cnt1[v] == cnt2[v]:
                matches += 1
            elif cnt1[v] == cnt2[v]+1:
                matches -= 1
            l+=1
        
        return matches == 26

            
