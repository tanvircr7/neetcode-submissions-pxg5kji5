class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s)==0:
            return 0
        
        dp = [[-1]*len(s) for _ in range(len(s))]

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):

                if s[i] == s[j]:
                    
                    if (j-i+1) <= 3 or dp[i+1][j-1]==1:

                        dp[i][j] = 1
        
        res = 0
        for i in range(len(s)):
            for j in range(len(s)):
                
                if dp[i][j]==1:
                    res += 1
        return res