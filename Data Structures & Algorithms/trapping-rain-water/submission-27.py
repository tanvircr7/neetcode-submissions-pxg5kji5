class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        h = height

        lmax = [0]*len(h)
        rmax = [0]*len(h)

        for i in range(1, len(h)):
            lmax[i] = max(lmax[i-1], h[i-1])
        for j in range(len(h)-2, -1, -1):
            rmax[j] = max(rmax[j+1], h[j+1])
        
        print(lmax)
        print(rmax)
        for i in range(len(h)):
            tmp = min(lmax[i], rmax[i])
            tmp -= h[i]
            ans += max(0, tmp)
        return ans
        
            

        






        
        