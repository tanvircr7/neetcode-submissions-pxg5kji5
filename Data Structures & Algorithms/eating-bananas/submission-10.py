class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)

        def getTime(rate):
            hours = 0
            for p in piles:
                hours += math.ceil(p/rate)
            return hours


        res = max(piles)
        while l<=r:
            rate = l+(r-l)//2

            if getTime(rate)<=h:
                res = rate
                r = rate-1
            else:
                l = rate+1
        
        return res