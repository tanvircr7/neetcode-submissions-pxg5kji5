class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def dp(val):
            if val==0:
                return 0
            
            if val in memo:
                return memo[val]
            
            cnt = 1e9

            for coin in coins:
                if val-coin >= 0:
                    cnt = min(cnt, dp(val-coin)+1)
            
            memo[val]=cnt

            return cnt
        
        val = dp(amount)

        return val if val!=1e9 else -1




        

