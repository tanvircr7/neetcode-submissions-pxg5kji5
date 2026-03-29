class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        h = height
        leftmax, rightmax = [0]*len(h), [0]*len(h)
        for i in range(1, len(h)):
            leftmax[i] = max(leftmax[i-1], h[i-1])
        for i in range(len(h)-2, -1, -1):
            rightmax[i] = max(rightmax[i+1], h[i+1])
        for i in range(len(h)):
            tmp = min(leftmax[i], rightmax[i])
            tmp -= h[i]
            ans += max(tmp, 0)
        return ans
        
            

        






        
        