class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def rec(i, holding):
            if i>=len(prices):
                return 0
            
            if (i,holding) in memo:
                return memo[(i,holding)]
            
            # do something
            v1 = 0
            if holding == True:
                v1 = rec(i+1, False) + prices[i]
            else:
                v1 = rec(i+1, True) - prices[i]
            
            # do nothing
            v2 = rec(i+1, holding)

            res = max(v1, v2)
            memo[(i,holding)] = res
            return res
        
        ans = rec(0, False)
        return ans