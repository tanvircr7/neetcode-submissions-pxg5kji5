class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        cnt1 = {i: 0 for i in range(26)}
        cnt2 = {i: 0 for i in range(26)}

        def table(c): return ord(c)-ord('a')

        for i in range(len(s1)):
            c = s1[i]
            cnt1[table(c)] += 1
        for i in range(len(s1)):
            c = s2[i]
            cnt2[table(c)] += 1
        matches = sum(cnt1[i]==cnt2[i] for i in range(26))

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            c = s2[r]
            cnt2[table(c)] += 1

            if cnt2[table(c)] == cnt1[table(c)]:
                matches += 1
            elif cnt2[table(c)] == cnt1[table(c)]+1:
                matches -= 1
            
            c = s2[l]
            cnt2[table(c)] -= 1
            if cnt2[table(c)] == cnt1[table(c)]:
                matches += 1
            elif cnt2[table(c)] == cnt1[table(c)]-1:
                matches -= 1
            l += 1
        
        if matches == 26:
            return True
        
        return False
                

        

            


        