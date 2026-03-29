class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def dp(amount):
            if amount in memo:
                return memo[amount]
            
            if amount == 0:
                return 0
            
            res = 1e9
            for coin in coins:
                if amount-coin>=0:
                    res = min(res, 1+dp(amount-coin))
            
            memo[amount] = res
            return memo[amount]
            
            
        
        return dp(amount) if dp(amount)!=1e9 else -1

