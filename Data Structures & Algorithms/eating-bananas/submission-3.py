class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        def days(k):
            val = 0
            for b in piles:
                val += math.ceil(b/k)
            return val

        l,r = 1, max(piles)
        ans = max(piles)

        while l<=r:
            k = l+(r-l)//2

            if days(k)<=h:
                r = k-1
                ans = min(ans, k)
            else:
                l = k+1
        

        return ans