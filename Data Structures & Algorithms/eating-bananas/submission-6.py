class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)

        def possible(rate):
            val = 0
            for n in piles:
                val += math.ceil(n/rate)
            print(f"{rate} = {val}")
            return val

        ans = max(piles)

        while l<=r:
            rate = l+(r-l) // 2

            if possible(rate)<=h:
                ans = min(ans, rate)
                r = rate-1
            else:
                l = rate+1
        
        return ans