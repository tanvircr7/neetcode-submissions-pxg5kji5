class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s)==0:
            return 0

        n = len(s)
        res = 0
        
        memo = [[-1]*n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):

                if s[i]==s[j]:

                    if (j-i+1) <=3 or memo[i+1][j-1]==1:
                        memo[i][j] = 1
                        res += 1


        return res