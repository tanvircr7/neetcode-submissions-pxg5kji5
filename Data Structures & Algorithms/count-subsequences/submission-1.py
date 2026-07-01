class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = [[-1]*len(t) for _ in range(len(s))]

        def f(i,j):
            if j==len(t):
                return 1
            if i==len(s):
                return 0
            
            if memo[i][j] != -1:
                return memo[i][j]
            
            res = 0
            # take
            if s[i]==t[j]:
                res = f(i+1,j+1)

            # no take
            res += f(i+1,j)
            memo[i][j] = res

            return res
        
        return f(0,0)