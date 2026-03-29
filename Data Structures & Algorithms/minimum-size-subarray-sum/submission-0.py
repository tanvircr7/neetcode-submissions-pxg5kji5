class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        ans = len(nums)+1
        sumX = 0

        for r in range(len(nums)):
            sumX += nums[r]

            while sumX >= target:
                ans = min(ans, r-l+1)
                
                sumX -= nums[l]
                l+=1
            
        
        return ans if ans<len(nums)+1 else 0
