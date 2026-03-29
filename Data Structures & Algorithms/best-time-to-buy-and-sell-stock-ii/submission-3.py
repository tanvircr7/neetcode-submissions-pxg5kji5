class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1]*2 for i in range(len(prices))]

        def rec(i, bought):
            if i>=len(prices):
                return 0
            
            if dp[i][bought] != -1:
                return dp[i][bought]

            res = rec(i+1, bought) # do nothing
            if bought:
                # if bough then sell
                res = max(res, prices[i]+rec(i+1, False))
            else:
                # if not bough then buy
                res = max(res, -prices[i]+rec(i+1, True))
            
            dp[i][bought] = res
            return res
        
        return rec(0, False)
