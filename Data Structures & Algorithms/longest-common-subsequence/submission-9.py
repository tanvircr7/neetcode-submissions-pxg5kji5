class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1]*len(text2) for i in range(len(text1))]

        def dfs(i,j):
            if i==len(text1) or j==len(text2):
                return 0
            
            if memo[i][j] != -1:
                return memo[i][j]
            res = 0
            if text1[i]==text2[j]:
                res = dfs(i+1,j+1)+1
            else:
                res = max(dfs(i,j+1), dfs(i+1,j))
            
            memo[i][j] = res
            return res
        
        return dfs(0,0)
