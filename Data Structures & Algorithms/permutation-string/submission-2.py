class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        cnt1 = [0]*26
        cnt2 = [0]*26

        for i in range(len(s1)):
            cnt1[ord(s1[i])-ord('a')] += 1

        for i in range(len(s1)):
            cnt2[ord(s2[i])-ord('a')] += 1

        matches = sum(cnt1[i]==cnt2[i] for i in range(26))

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            val = ord(s2[r])-ord('a')
            cnt2[val] += 1
            
            if cnt1[val] == cnt2[val]:
                matches += 1
            elif cnt1[val] == cnt2[val]-1:
                matches -= 1
            
            val = ord(s2[l]) - ord('a')
            cnt2[val] -= 1

            if cnt1[val] == cnt2[val]:
                matches += 1
            elif cnt1[val] -1 == cnt2[val]:
                matches -= 1
            l += 1
        
        return matches == 26
            
        

            


        