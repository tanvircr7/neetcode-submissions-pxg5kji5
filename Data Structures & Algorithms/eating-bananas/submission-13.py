class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def day(rate):
            res = 0
            for n in piles:
                res += math.ceil(n/rate)
            return res
        
        l,r = 1, max(piles)
        ans = 0

        while l<=r:
            m = l+(r-l)//2

            days = day(m)

            if days <= h:
                r = m-1
                ans = m
            else:
                l = m+1
        
        return ans
