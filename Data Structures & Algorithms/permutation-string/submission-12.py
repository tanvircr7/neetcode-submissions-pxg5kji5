class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        func = lambda c: ord(c)-ord('a')

        cnt1 = {i:0 for i in range(26)}
        for c in s1:
            cnt1[func(c)] = cnt1.get(func(c),0)+1
        cnt2 = {i:0 for i in range(26)}
        for i in range(len(s1)):
            c = s2[i]       
            cnt2[func(c)] = cnt2.get(func(c), 0)+1
        
        matches = sum(cnt1[i]==cnt2[i] for i in range(26))
        l=0

        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            c = s2[r]
            cnt2[func(c)] = cnt2.get(func(c),0)+1

            x = func(c)
            if cnt1[x] == cnt2[x]:
                matches += 1
            elif cnt1[x] == cnt2[x]-1:
                matches -= 1
            
            x = func(s2[l])
            cnt2[x] -= 1
            
            if cnt1[x] == cnt2[x]:
                matches += 1
            elif cnt1[x] == cnt2[x]+1:
                matches -=1

            l+=1
        
        return True if matches==26 else False

        

            
