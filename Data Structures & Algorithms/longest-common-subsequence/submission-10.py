class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1]*len(text2) for i in range(len(text1))]

        def f(i,j):
            if i==len(text1) or j==len(text2):
                return 0
            
            if memo[i][j] != -1:
                return memo[i][j]
            
            res = 0
            if text1[i] == text2[j]:
                res = f(i+1,j+1)+1
            else:
                res = max(f(i+1,j), f(i,j+1))
            
            memo[i][j] = res
            return res
        
        return f(0,0)
