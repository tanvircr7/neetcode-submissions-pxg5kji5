class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l, r = 0, len(height)-1
        h = height
        maxL = h[l]
        maxR = h[r]

        res = 0
        while l<r:
            if maxL<maxR:
                l+=1
                val = maxL-h[l]
                if val>0:
                    res += val
                maxL = max(maxL, h[l])
            else:
                r-=1
                val = maxR-h[r]
                if val>0:
                    res+= val
                maxR = max(maxR, h[r])
        
        return res