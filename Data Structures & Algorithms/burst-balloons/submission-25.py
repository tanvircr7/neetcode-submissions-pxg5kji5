class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n=len(nums)
        xnums = [1]+nums+[1]

        dp = [[0]*len(xnums) for _ in range(len(xnums))]

        for l in range(n, -1, -1):
            for r in range(l, n+1):

                for i in range(l,r+1):
                    coins = xnums[l-1]*xnums[i]*xnums[r+1]
                    coins += dp[l][i-1] + dp[i+1][r]
                    dp[l][r] = max(dp[l][r], coins)
        
        return dp[1][n]
                