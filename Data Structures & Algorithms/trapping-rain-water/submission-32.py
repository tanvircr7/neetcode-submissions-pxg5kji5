class Solution:
    def trap(self, h: List[int]) -> int:
        ans = 0
        
        minL = h[0]
        minR = h[len(h)-1]

        l, r=  0, len(h)-1

        while l<=r:

            if minL <= minR:

                tmp = minL - h[l]
                ans += max(0, tmp)
                minL = max(minL, h[l])
                l+=1
            else:

                tmp = minR - h[r]
                ans += max(0, tmp)
                minR = max(minR, h[r])
                r-=1
        
        return ans





        
        