class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0

        for i in range(len(nums)):
            print(maxReach)
            jump = nums[i]
            if i<=maxReach:
                maxReach  = max(maxReach, i+jump)
        
        return maxReach >= len(nums)-1
