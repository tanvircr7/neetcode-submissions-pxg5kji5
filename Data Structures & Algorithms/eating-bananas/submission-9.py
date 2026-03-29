class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)

        def day(rate):
            cnt = 0
            for p in piles:
                tmp = math.ceil(p/rate)
                cnt += tmp
            return cnt

        while l<=r:
            m = l+(r-l) // 2

            if day(m) <= h:
                ans = m
                r = m-1
            else:
                l = m+1
        
        return ans