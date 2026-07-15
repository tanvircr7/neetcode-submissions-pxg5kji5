class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1), len(word2)

        memo = [[-1]*(n) for _ in range(m)]


        def f(i,j):
            if i==m:
                return n-j
            if j==n:
                return m-i
            
            if memo[i][j] != -1:
                return memo[i][j]
            
            res = 0
            if word1[i]==word2[j]:
                res = f(i+1,j+1)
            else:
                delete = f(i+1,j)
                insert = f(i,j+1)
                res = min(delete, insert, f(i+1,j+1)) + 1
            
            memo[i][j] = res
            return res
        
        return f(0,0)