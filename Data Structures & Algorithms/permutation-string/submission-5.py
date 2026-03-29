class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        def lookup(c):
            return ord(c)-ord('a')

        m1 = {i:0 for i in range(26)}
        m2 = {i:0 for i in range(26)}
        for i in range(len(s1)):
            m1[lookup(s1[i])] += 1
            m2[lookup(s2[i])] += 1
        
        matches = sum(m1[i]==m2[i] for i in range(26))

        l=0
        
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            # print(matches)
            curr = s2[r]

            m2[lookup(curr)] += 1
            if m2[lookup(curr)] == m1[lookup(curr)]:
                matches += 1
            elif m2[lookup(curr)] == m1[lookup(curr)]+1:
                matches -= 1
            
            curr = s2[l]
            m2[lookup(curr)] -= 1
            if m2[lookup(curr)] == m1[lookup(curr)]:
                matches += 1
            elif m2[lookup(curr)] == m1[lookup(curr)]-1:
                matches -= 1
            l += 1
        
        if matches == 26:
            return True
        
        return False
        

            


        