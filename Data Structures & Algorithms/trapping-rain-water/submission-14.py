class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        h = height

        l,r=0, len(h)-1
        minL, minR = h[0], h[len(h)-1]

        while l<r:
            if minL<minR:
                x = minL-h[l]
                ans += max(0,x)
                l+=1
                minL = max(minL, h[l])
            else:
                y = minR-h[r]
                ans += max(0,y)
                r-=1
                minR = max(minR, h[r])

        
        return ans
            

        






        
        