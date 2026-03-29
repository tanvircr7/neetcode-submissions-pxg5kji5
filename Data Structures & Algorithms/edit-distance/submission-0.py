class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        def f(i,j):
            if i==m:
                return n-j
            if j==n:
                return m-i
            
            if word1[i]==word2[j]:
                return f(i+1, j+1)

            res = min( f(i+1,j), f(i,j+1))
            res = min(res, f(i+1,j+1))
            res += 1

            return res
        
        return f(0,0)