class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxr = 0

        for i in range(len(nums)):
            jump = nums[i]

            if i<=maxr:
                maxr = max(maxr, i+jump)
            
        return maxr >= len(nums)-1