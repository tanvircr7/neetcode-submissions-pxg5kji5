class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        res = 0
        h = heights
        
        while l<r:

            res = max(res, min(h[l],h[r])*(r-l) )

            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        
        return res