class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        GG = 1e9

        def f(val):
            if val==0:
                return 0
            
            if val in memo:
                return memo[val]
            
            res = GG
            for c in coins:
                if val-c >= 0:
                    res = min(res, f(val-c)+1)
            
            memo[val] = res

            return res
    

        ans = f(amount)

        return ans if ans!=GG else -1

