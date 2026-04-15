class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m = len(word1)
        n = len(word2)
        memo = [[-1]*(n+1) for i in range(m+1)]


        def f(i,j):
            if i==m:
                return n-j
            if j==n:
                return m-i
            
            if memo[i][j] != -1:
                return memo[i][j]
            
            res = -1
            if word1[i] == word2[j]:
                res = f(i+1,j+1)
            else:
                insert = f(i,j+1)
                delete = f(i+1,j)
                replace = f(i+1,j+1)
                res = min(insert, delete, replace)
                res += 1
            
            memo[i][j] = res
            return res
        
        return f(0,0)