class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[-1]*(len(word2)+1) for i in range(len(word1)+1)]
        res = 0
        m,n = len(word1), len(word2)

        def f(i,j):
            if i==len(word1):
                return n-j
            if j==len(word2):
                return m-i
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            res = 0
            if word1[i] == word2[j]:
                res = f(i+1,j+1)
            else:
                insert = f(i,j+1)
                delete = f(i+1,j)
                replace = f(i+1,j+1)
                res = min(insert, delete, replace)
                res += 1
            
            dp[i][j] = res
            return res
        
        return f(0,0)
