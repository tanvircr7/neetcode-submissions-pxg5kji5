class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]
            
            if i == 0:
                return 0
            
            res = 1e9
            for coin in coins:
                if i-coin >=0:
                    res = min(res, dp(i-coin)+1)
            
            memo[i] = res
            return memo[i]

        
        ans = dp(amount)
        return ans if ans != 1e9 else -1