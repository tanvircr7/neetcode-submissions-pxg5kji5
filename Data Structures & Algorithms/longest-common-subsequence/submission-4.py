class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1]*len(text2) for _ in range(len(text1))]

        def f(i,j):
            if i<0 or j<0:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]
            
            if text1[i] == text2[j]:
                val = 1 + f(i-1,j-1)
            else:
                val = max( f(i,j-1), f(i-1,j) )

            memo[i][j] = val
            return val
        
        val = f(len(text1)-1, len(text2)-1)
        print(memo)
        return val
