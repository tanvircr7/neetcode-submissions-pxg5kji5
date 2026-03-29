class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        h = height

        maxL, maxR = 0,0
        l, r = 0, len(h)-1

        while l<=r:
            if maxL <= maxR:
                tmp = maxL - h[l]
                print(f"left {tmp}")
                ans += max(0, tmp)
                maxL = max(maxL, h[l])
                l += 1
            else:
                tmp = maxR - h[r]
                print(f"left {tmp}")
                ans += max(0, tmp)
                maxR = max(maxR, h[r])
                r -= 1
        
        return ans
        

        






        
        