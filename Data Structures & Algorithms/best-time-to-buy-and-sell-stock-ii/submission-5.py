class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}

        def f(i, holding):
            if i>=len(prices):
                return 0
            
            if (i,holding) in memo:
                return memo[(i,holding)]
            
            v1 = 0
            if holding==False:
                v1 = f(i+1, True) - prices[i]
            elif holding == True:
                v1 = f(i+1, False) + prices[i]

            v2 = f(i+1, holding)

            res = max(v1, v2)
            memo[(i,holding)] = res
            return res

        

        return f(0, False)
