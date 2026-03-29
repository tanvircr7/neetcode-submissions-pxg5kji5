class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        h = height
        minleft, minright = h[0], h[len(h)-1]
        l,r = 0, len(h)-1
        while l<=r:
            if minleft < minright:
                tmp = minleft-h[l]
                ans += max(0, tmp)
                minleft = max(minleft, h[l])
                l+=1
            else:
                tmp = minright-h[r]
                ans += max(0, tmp)
                minright = max(minright, h[r])
                r-=1

        return ans
        
            

        






        
        