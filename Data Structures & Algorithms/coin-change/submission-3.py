class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def f(amount):
            if amount in memo:
                return memo[amount]
            
            if amount == 0:
                return 0
            
            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1+f(amount-coin))
            
            memo[amount] = res
            return memo[amount]
        
        return f(amount) if f(amount)!=1e9 else -1