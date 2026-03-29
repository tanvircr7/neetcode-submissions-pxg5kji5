class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        h = height

        l,r=0, len(h)-1
        minL, minR = h[l], h[r]

        while l<=r:
            if minL<minR:
                tmp = minL-h[l]
                ans += max(0, tmp)
                l+=1
                minL = max(minL, h[l])
            else:
                tmp = minR-h[r]
                ans += max(0, tmp)
                r-=1
                minR = max(minR, h[r])

        
        return ans
            

        






        
        