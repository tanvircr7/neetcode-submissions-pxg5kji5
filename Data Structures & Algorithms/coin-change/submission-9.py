class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def dp(val):
            if val in memo:
                return memo[val]
            
            if val==0:
                return 0
            
            total = 1e9
            for coin in coins:
                if val-coin>=0:
                    total = min(total, dp(val-coin)+1)
            
            memo[val] = total
            return memo[val]
        
        val = dp(amount)

        return val if val!=1e9 else -1


        

