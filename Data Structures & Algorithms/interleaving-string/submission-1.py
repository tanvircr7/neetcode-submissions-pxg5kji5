class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3):
            return False
        
        dp = {}

        def f(i,j,k):
        
            if k==len(s3):
                return (i==len(s1)) and (j==len(s2))
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            take1, take2 = False, False
            if i<len(s1) and s1[i] == s3[k]:
                take1 = f(i+1,j,k+1)
            
            if j<len(s2) and s2[j] == s3[k]:
                take2 = f(i,j+1,k+1)

            res = take1 or take2
            dp[(i,j)] = res
            return res
        
        return f(0,0,0)