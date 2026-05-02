class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        ans = r

        def daycnt(rate):
            res = 0
            for n in piles:
                res += math.ceil(n/rate)
            return res
        
        while l<=r:
            rate = l+(r-l)//2
            days = daycnt(rate)

            if days <= h:
                ans = rate
                r = rate-1
            else:
                l = rate+1
        
        return  ans