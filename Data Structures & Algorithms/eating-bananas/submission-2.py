class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        def time(k):
            hrs = 0
            for bananas in piles:
                hrs += math.ceil(bananas/k)
            print(hrs)
            return hrs


        while l<=r:
            m = l+(r-l) // 2

            if time(m)<=h:
                res = min(res, m)
                r = m-1
            
            elif time(m)>h:
                l = m+1
        
        return res