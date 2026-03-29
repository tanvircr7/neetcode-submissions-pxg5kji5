class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = [[-1]*(len(word2)+1) for i in range(len(word1)+1)]

        def f(i,j):
            if i==m:
                return n-j
            if j==n:
                return m-i
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if word1[i]==word2[j]:
                dp[i][j] = f(i+1,j+1)
            else:
                res = f(i+1,j) # delete
                res = min(res, f(i,j+1)) # insert
                res = min(res, f(i+1,j+1)) # swap
                dp[i][j] = res+1 # cost for operation

            return dp[i][j]
        
        return f(0,0)