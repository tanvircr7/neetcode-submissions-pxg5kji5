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
        
        matches = sum(cnt1[k] == cnt2[k] for k in range(26))

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            idx = ord(s2[r]) - ord('a')
            cnt2[idx] += 1
            if cnt2[idx] == cnt1[idx]:
                matches += 1
            elif cnt2[idx] -1 == cnt1[idx]:
                matches -= 1

            idx = ord(s2[l]) - ord('a')
            cnt2[idx] -= 1
            if cnt2[idx] == cnt1[idx]:
                matches += 1
            elif cnt2[idx] +1 == cnt1[idx]:
                matches -= 1
            l += 1

        return matches == 26
            

            
        

            


        