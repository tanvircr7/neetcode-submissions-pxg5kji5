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
            m = l+(r-l)//2
            cnt = daycnt(m)

            if cnt<=h:
                ans = m
                r = m-1
            else:
                l = m+1
        
        return ans