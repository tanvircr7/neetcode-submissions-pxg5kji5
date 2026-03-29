class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        leftMax = [0]*n
        rightMax = [0]*n

        h = height
        leftMax[0] = 0
        for i in range(1,n):
            leftMax[i] = max(leftMax[i-1], h[i-1])



        rightMax[n-1] = 0
        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], h[i+1])


        res = 0

        for i in range(n):
            water = min(leftMax[i], rightMax[i]) - height[i]
            # Only add if positive (water can't be negative)
            res += max(0, water)
        
        return res

        
        