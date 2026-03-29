class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        
        f = lambda k: ord(k)-ord('a')
        cnt1 = {i:0 for i in range(26)}
        for c in s1:
            cnt1[f(c)] = cnt1.get(f(c),0)+1
        cnt2 = {i:0 for i in range(26)}
        for i in range(len(s1)):
            c = s2[i]
            cnt2[f(c)] = cnt2.get(f(c),0)+1
        
        matches = sum(cnt1[i]==cnt2[i] for i in range(26))

        l=0
        for r in range(len(s1), len(s2)):
            c = s2[r]
            cnt2[f(c)] += 1

            if matches == 26:
                return True
            
            if cnt2[f(c)] == cnt1[f(c)]:
                matches += 1
            elif cnt2[f(c)]-1 == cnt1[f(c)]:
                matches -= 1
            
            c = s2[l]
            cnt2[f(c)] -= 1

            if cnt2[f(c)] == cnt1[f(c)]:
                matches += 1
            elif cnt2[f(c)]+1 == cnt1[f(c)]:
                matches -= 1
            l+=1
        
        if matches == 26:
            return True
        
        return False

            
