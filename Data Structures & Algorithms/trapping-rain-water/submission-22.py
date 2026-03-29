class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        h = height
        lmax = h[0]
        rmax = h[len(h)-1]
        l,r = 0, len(h)-1

        while l<=r:
            if lmax<rmax:
                tmp = lmax-h[l]
                ans += max(0, tmp)
                lmax = max(lmax, h[l])
                l+=1
            else:
                tmp = rmax-h[r]
                ans += max(0, tmp)
                rmax = max(rmax, h[r])
                r-=1
        
        return ans

        
            

        






        
        