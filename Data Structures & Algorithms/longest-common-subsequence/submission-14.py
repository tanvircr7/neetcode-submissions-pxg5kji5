class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1), len(text2)

        memo = [[-1]*(n+1) for i in range(m+1)]


        def f(i,j):
            if i==m:
                return 0
            if j==n:
                return 0
            
            if memo[i][j] != -1:
                return memo[i][j]
            
            res = 0
            if text1[i]==text2[j]:
                res = f(i+1,j+1)+1
            else:
                res = max( f(i+1,j), f(i,j+1) )
            
            memo[i][j] = res

            return res
        
        return f(0,0)