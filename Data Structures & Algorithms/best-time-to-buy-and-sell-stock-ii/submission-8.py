class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        memo = {}

        def f(i, holding):

            if i==len(prices):
                return 0
            
            if (i,holding) in memo:
                return memo[(i,holding)]
            
            sellval, buyval = 0, 0
            if holding == True:
                sellval = f(i+1, False) + prices[i]
            else:
                buyval = f(i+1, True) - prices[i]
            
            donothing = f(i+1, holding)

            res = max(sellval, buyval, donothing)

            memo[(i,holding)] = res

            return res

        
        ans = f(0, False)

        return ans