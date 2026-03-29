class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def f(val):
            if val in memo:
                return memo[val]
                
            if val==0:
                return 0
            
            res = 1e9
            for c in coins:
                if val-c >= 0:
                    res = min(res, f(val-c)+1)
            
            memo[val] = res
            return res

        coinsNeeded = f(amount)
        return coinsNeeded if coinsNeeded != 1e9 else -1

        

