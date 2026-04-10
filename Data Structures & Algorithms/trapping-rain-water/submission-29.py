class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        lmax = [0]*len(height)
        rmax = [0]*len(height)

        for i in range(1, len(lmax)):
            lmax[i] = max(lmax[i-1], height[i-1])
        for i in range(len(rmax)-2, -1, -1):
            rmax[i] = max(rmax[i+1], height[i+1])
        
        for i in range(len(height)):
            tmp = min(lmax[i], rmax[i])
            tmp = tmp - height[i]
            ans += max(0, tmp)
        
        return ans

        
            

        






        
        