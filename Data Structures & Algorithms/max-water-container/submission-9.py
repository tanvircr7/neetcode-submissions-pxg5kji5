class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        h = heights
        ans = 0
        func = lambda x,i,y,j: (j-i)*min(x,y)

        while l<r:
            ans = max(ans, func(h[l], l, h[r], r))

            if h[l] < h[r]:
                l+=1
            else:
                r-=1
        
        return ans
