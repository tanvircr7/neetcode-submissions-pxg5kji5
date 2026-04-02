class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        ans = r

        def totaltime(rate):
            res = 0
            for n in piles:
                res += math.ceil(n/rate)
            return res

        while l<=r:
            k = l + (r-l) // 2

            d = totaltime(k)

            if d<=h:
                ans = k
                r = k-1
            else:
                l = k+1
        
        return ans
