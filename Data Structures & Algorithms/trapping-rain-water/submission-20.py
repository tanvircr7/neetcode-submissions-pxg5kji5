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
                lmin = max(lmin, h[l])
                l+=1
            else:
                tmp = rmin - h[r]
                ans += max(0, tmp)
                rmin = max(rmin, h[r])
                r-=1
        
        return ans
        
            

        






        
        