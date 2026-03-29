class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        h = height
        l,r = 0, len(h)-1
        lmax = h[l]
        rmax = h[r]

        while l<=r:
            if lmax<rmax:
                tmp = lmax-h[l]
                ans += max(0, tmp)
                l += 1
                lmax = max(lmax, h[l])
            else:
                tmp = rmax-h[r]
                ans += max(0, tmp)
                r-=1
                rmax = max(rmax, h[r])
        
        return ans
        
            

        






        
        