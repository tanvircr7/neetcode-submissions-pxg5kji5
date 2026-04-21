class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n=len(nums)

        num1 = [1]+nums+[1]

        dp = [[0]*(n+2) for _ in range(n+2)]

        for l in range(n, 0, -1):
            for r in range(l, n+1):

                for i in range(l, r+1):

                    coins = num1[l-1]*num1[i]*num1[r+1]
                    coins += dp[l][i-1] + dp[i+1][r]
                    dp[l][r] = max(dp[l][r], coins)
        
        return dp[1][n]