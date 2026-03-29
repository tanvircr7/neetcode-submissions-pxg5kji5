class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        cnt1 = [0]*26
        cnt2 = [0]*26
        idx = lambda x: ord(x)-ord('a')

        for i in range(len(s1)):
            cnt1[idx(s1[i])] += 1
        for i in range(len(s1)):
            cnt2[idx(s2[i])] += 1
        matches = sum(cnt1[i]==cnt2[i] for i in range(26))

        l=0
        for r in range(len(s1),len(s2)):
            if matches == 26:
                return True
            
            cnt2[idx(s2[r])]+=1
            if cnt2[idx(s2[r])] == cnt1[idx(s2[r])]:
                matches += 1
            elif cnt2[idx(s2[r])] == cnt1[idx(s2[r])] + 1:
                matches -= 1
            
            cnt2[idx(s2[l])] -= 1
            if cnt2[idx(s2[l])] == cnt1[idx(s2[l])]:
                matches += 1
            elif cnt2[idx(s2[l])] + 1 == cnt1[idx(s2[l])]:
                matches -= 1
            l += 1
        
        return matches == 26
            
        

            


        