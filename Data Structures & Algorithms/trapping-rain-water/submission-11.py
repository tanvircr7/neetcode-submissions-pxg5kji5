class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        h = height
        leftMax = [0 for i in range(len(h))]
        rightMax = [0 for i in range(len(h))]

        for i in range(1,len(h)):
            leftMax[i] = max(leftMax[i-1], h[i-1])
            print(leftMax[i])
        print("-=======")
        
        for i in range(len(h)-2, 0, -1):
            rightMax[i] = max(rightMax[i+1], h[i+1])
            print(rightMax[i])
        print("-=======")

        
        for i in range(len(h)):
            tmp = min(leftMax[i], rightMax[i])
            tmp -= h[i]
            print(tmp)
            ans += max(0, tmp)
        return ans
        

        






        
        