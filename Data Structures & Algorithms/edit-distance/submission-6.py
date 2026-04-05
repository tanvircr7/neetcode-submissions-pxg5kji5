class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        memo = [[-1]*(len(word2)+1) for i in range(len(word1)+1)]

        m,n = len(word1), len(word2)

        def f(i,j):
            if i==len(word1):
                return n-j
            if j==len(word2):
                return m-i
            
            if memo[i][j] != -1:
                return memo[i][j]
            
            res = 0
            if word1[i] == word2[j]:
                res = f(i+1,j+1)
            else:
                insert = f(i+1, j)
                delete = f(i,j+1)
                replace = f(i+1,j+1)
                cost = min(insert, delete, replace)
                cost += 1
                res = cost

            memo[i][j] = res
            return res
        
        return f(0,0)