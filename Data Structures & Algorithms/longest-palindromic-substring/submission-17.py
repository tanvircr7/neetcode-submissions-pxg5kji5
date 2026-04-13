class Solution:
    def longestPalindrome(self, s: str) -> str:
        n= len(s)
        if n==0:
            return 0
        
        memo = [[-1]*n for i in range(n)]
        residx, reslen = -1, 0

        for i in range(n-1, -1, -1):
            for j in range(i, n):

                if s[i]==s[j]:

                    if j-i+1 <= 3 or memo[i+1][j-1]==1:

                        if j-i+1 > reslen:
                            reslen = j-i+1
                            residx = i
                        
                        memo[i][j] = 1


        return s[residx: residx+reslen]






        
