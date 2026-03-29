class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        h = height
        
        leftMax = [0 for i in range(n)]
        for i in range(1,n):
            leftMax[i] = max(h[i-1], leftMax[i-1])


        rightMax = [0 for i in range(n)]
        for i in range(n-2, -1, -1):
            rightMax[i] = max(h[i+1], rightMax[i+1])

        ans = 0

        for i in range(1, n):
            val = min(leftMax[i], rightMax[i])-h[i]
            ans += max(0, val)
        
        return ans



        
        