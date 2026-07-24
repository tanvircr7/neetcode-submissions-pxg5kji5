class Solution:
    def trap(self, h: List[int]) -> int:
        res = 0
        minL, minR = h[0], h[-1]
        l, r= 0, len(h)-1

        while l<=r:
            if minL<minR:
                tmp = minL-h[l]
                res += max(0, tmp)
                minL = max(minL, h[l])
                l+=1
            else:
                tmp = minR-h[r]
                res += max(0, tmp)
                minR = max(minR, h[r])
                r-=1
        
        return res
        