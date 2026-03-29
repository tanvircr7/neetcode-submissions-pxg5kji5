class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j,k= 0,0,0
        n1 = len(word1)
        n2 = len(word2)
        ans = ""
        while i<n1 and j<n2:
            ans = ans + word1[i]
            ans = ans + word2[j]
            i+=1
            j+=1
        
        while i<n1:
            ans = ans + word1[i]
            i+=1
        
        while j<n2:
            ans = ans + word2[j]
            j+=1
        
        return ans