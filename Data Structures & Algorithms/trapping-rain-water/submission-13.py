class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        h = height

        leftMax = [0]*len(h)
        for i in range(1, len(h)):
            leftMax[i] = max(h[i-1], leftMax[i-1])

        rightMax = [0]*len(h)
        for i in range(len(h)-2, -1, -1):
            rightMax[i] = max(h[i+1], rightMax[i+1])
        
        for i in range(len(h)):
            minheight = min(leftMax[i], rightMax[i])
            add = minheight - h[i]
            ans += max(0, add)
        
        return ans
            

        






        
        