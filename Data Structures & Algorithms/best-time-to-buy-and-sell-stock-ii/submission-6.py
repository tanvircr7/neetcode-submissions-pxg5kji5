class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}
        
        def rec(i, holding):

            if i>=len(prices):
                return 0
            
            if (i,holding) in memo:
                return memo[(i,holding)]
            
            res = 0
            donothing = rec(i+1, holding)
            do = 0
            if holding == True:
                do = rec(i+1, False)+prices[i]
            else:
                do = rec(i+1, True)-prices[i]
            
            res = max(donothing, do)
            
            memo[(i,holding)] = res
            return res


        

        return rec(0, False)
