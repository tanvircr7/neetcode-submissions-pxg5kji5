class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}

        def f(i, holding):

            if i==len(prices):
                return 0
            
            if (i,holding) in memo:
                return memo[(i,holding)]
            
            sell, buy = 0, 0
            if holding == True:
                sell = f(i+1, False) + prices[i]
            else:
                buy = f(i+1, True) - prices[i]
            
            donothing = f(i+1, holding)

            res = max(sell, buy, donothing)

            memo[(i,holding)] = res
            return res


        
        return f(0, False)