class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}

        def f(i, bought):
            if i>=len(prices):
                return 0
            
            if (i,bought) in memo:
                return memo[(i,bought)]
            
            v1 = 0
            if bought==False:
                v1 = f(i+1, True) - prices[i]
            elif bought == True:
                v1 = f(i+1, False) + prices[i]
                
            v2 = f(i+1, bought)

            res = max(v1, v2)
            memo[(i,bought)] = res
            return res

        

        return f(0, False)
