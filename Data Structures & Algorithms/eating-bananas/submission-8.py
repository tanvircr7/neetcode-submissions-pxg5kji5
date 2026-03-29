class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)

        def daycnt(rate):
            res = 0
            for p in piles:
                res += math.ceil(p/rate)
            print(res)
            return res

        ans = r
        while l<=r:
            m = l+(r-l)//2

            if daycnt(m) <= h:
                ans = min(ans, m)
                r=m-1
            else:
                l=m+1

        return ans