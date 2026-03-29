class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        if n==0:
            return ""

        dp = [[-1]*n for i in range(n)]
        reslen, residx = -1, -1

        for i in range(n-1,-1,-1):
            for j in range(i,n):

                if s[i]==s[j]:
                    
                    if (j-i+1)<=3 or dp[i+1][j-1]==1:
                        dp[i][j] = 1

                        if j-i+1 > reslen:
                            reslen = j-i+1
                            residx = i
        
        cnt = 0
        for i in range(n):
            for j in range(n):
                if dp[i][j]==1:
                    cnt += 1
        
        return cnt