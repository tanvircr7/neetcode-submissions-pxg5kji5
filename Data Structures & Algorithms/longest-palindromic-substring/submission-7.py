class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n==0:
            return ""

        residx, reslen = -1, -1

        dp = [[-1]*n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                
                if s[i]==s[j]:
                    if (j-i+1) <=3 or dp[i+1][j-1]==1:
                        dp[i][j] = 1

                        if j-i+1>reslen:
                            reslen = j-i+1
                            residx = i
        
        return s[residx: residx+reslen]

        
