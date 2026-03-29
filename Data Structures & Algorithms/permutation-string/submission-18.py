class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        func = lambda c: ord(c)-ord('a')
        cnt1 = {i:0 for i in range(26)}
        cnt2 = {i:0 for i in range(26)}
        for c in s1:
            x = func(c)
            cnt1[x] = cnt1.get(x,0)+1
        for i in range(len(s1)):
            x = func(s2[i])
            cnt2[x] = cnt2.get(x,0)+1
        matches = sum(cnt1[i]==cnt2[i] for i in range(26))
        l=0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            x = func(s2[r])
            cnt2[x] = cnt2.get(x,0)+1

            if cnt2[x] == cnt1[x]:
                matches += 1
            elif cnt2[x] - 1 == cnt1[x]:
                matches -= 1
            
            x = func(s2[l])
            cnt2[x] -= 1
            if cnt2[x] == cnt1[x]:
                matches += 1
            elif cnt2[x] + 1 == cnt1[x]:
                matches -= 1

            l+=1
            
        
        return True if matches == 26 else False
