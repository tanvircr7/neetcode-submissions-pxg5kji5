class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1]*len(text2) for _ in range(len(text1))]

        def dfs(i,j):
            if i<0 or j<0:
                return 0
            
            if memo[i][j] != -1:
                return memo[i][j]
            
            val = 0
            if text1[i]==text2[j]:
                val = 1+dfs(i-1,j-1)
            else:
                val = max(dfs(i,j-1), dfs(i-1,j))

            memo[i][j] = val
            return val
        

        return dfs(len(text1)-1, len(text2)-1)