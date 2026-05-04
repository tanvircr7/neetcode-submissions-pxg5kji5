class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1), len(word2)

        dp = [[-1]*n for i in range(m)]

        def f(i,j):
            if i==m:
                return n-j
            if j==n:
                return m-i
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            res = 0
            if word1[i]==word2[j]:
                res = f(i+1,j+1)
            else:
                insert = f(i,j+1)
                delete = f(i+1,j)
                replace = f(i+1,j+1)
                res = min(insert, delete, replace)+1
            
            dp[i][j] = res
            return res
        
        return f(0,0)