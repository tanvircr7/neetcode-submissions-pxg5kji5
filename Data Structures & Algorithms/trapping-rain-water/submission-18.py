class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        h = height
        lmin=h[0]
        rmin=h[len(h)-1]

        l,r = 0, len(h)-1
        while l<=r:
            if lmin<rmin:
                tmp = lmin-h[l]
                ans += max(0, tmp)
                l+=1
                lmin = max(lmin, h[l])
            else:
                tmp = rmin - h[r]
                ans += max(0, tmp)
                r-=1
                rmin = max(rmin, h[r])
        
        return ans
        
            

        






        
        