class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxreach = 0

        for i in range(len(nums)):
            jump = nums[i]
            
            if i<=maxreach:
                maxreach = max(maxreach, i+jump)
            
        
        return maxreach >= (len(nums)-1)