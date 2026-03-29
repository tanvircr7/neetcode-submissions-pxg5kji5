class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        step = [prices[i+1]-prices[i] for i in range(len(prices)-1)]

        ans = 0
        for s in step:
            if s>0:
                ans += s
        return ans