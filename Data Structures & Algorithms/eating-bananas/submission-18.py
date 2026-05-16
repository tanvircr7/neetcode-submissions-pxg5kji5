class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def daycnt(rate):
            res = 0
            for n in piles:
                res += math.ceil(n/rate)
            return res

        l,r = 1, max(piles)
        ans = r

        while l<=r:
            rate = l+(r-l)//2

            if daycnt(rate) <= h:
                ans = rate
                r = rate-1
            else:
                l = rate+1
        
        return ans