class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1), len(word2)

        memo = [[-1]*(n+1) for _ in range(m+1)]

        def f(i,j):
            if i==m:
                return n-j
            if j==n:
                return m-i
            
            res = 0
            
            if memo[i][j] != -1:
                return memo[i][j]
            
            if word1[i]==word2[j]:
                res = f(i+1,j+1)
            else:
                sub = f(i+1,j+1)
                insert = f(i,j+1)
                delete = f(i+1,j)
                res = min(sub, insert, delete)+1
            
            memo[i][j] = res
            return res
        
        return f(0,0)