class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = [[-1]*len(word2) for i in range(len(word1))]

        def f(i,j):
            if i==m:
                return n-j
            if j==n:
                return m-i
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if word1[i]==word2[j]:
                dp[i][j] = f(i+1, j+1)
            else:
                res = min( f(i+1,j), f(i,j+1))
                res = min(res, f(i+1,j+1))
                res += 1
                dp[i][j] = res

            return dp[i][j]
        
        return f(0,0)