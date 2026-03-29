class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}   
        memo[0] = 0

        def f(val):
            if val in memo:
                return memo[val]
            
            res = 1e9
            for c in coins:
                if val-c >= 0:
                    res = min(res, 1 + f(val-c))
            
            memo[val] = res
            return res
        
        ans = f(amount)
        return ans if ans!=1e9 else -1
            


