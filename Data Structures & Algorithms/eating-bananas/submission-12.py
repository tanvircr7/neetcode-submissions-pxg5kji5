class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def days(rate):
            res = 0
            for p in piles:
                res += math.ceil(p/rate)
            return res

        
        l,r = 1, max(piles)
        ans = max(piles)

        while l<=r:
            rate = l+(r-l)//2

            if days(rate) <= h:
                r = rate - 1
                ans = rate
            else:
                l = rate+1
        
        return ans
