class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def dp(val):
            if val in memo:
                return memo[val]
            
            if val == 0:
                return 0
            
            res = 1e9
            for coin in coins:
                if val-coin >= 0:
                    res = min(res, dp(val-coin)+1)
            
            memo[val] = res
            return res
        
        ans = dp(amount)
        return ans if ans < 1e9 else -1




        

