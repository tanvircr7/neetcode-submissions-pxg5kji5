class Solution:
    def trap(self, h: List[int]) -> int:
        ans = 0
        lmax = [0]*(len(h))
        rmax = [0]*(len(h))

        for i in range(1, len(h)):
            lmax[i] = max(lmax[i-1], h[i-1])
        
        for i in range(len(h)-2, -1, -1):
            rmax[i] = max(rmax[i+1], h[i+1])
        
        for i in range(len(h)):
            tmp = min(lmax[i], rmax[i])
            tmp = tmp - h[i]

            ans += max(0, tmp)
        
        return ans



        
        