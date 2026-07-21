class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.qsh(0, len(nums)-1, nums)
        return nums
    
    def qsh(self, s, e, nums):

        if e-s+1<=1:
            return 
        import random
        pivot = random.randint(s,e)
        nums[pivot], nums[e] = nums[e], nums[pivot]
        left = s
        for i in range(s, e):
            if nums[i] <= nums[e]:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
        
        nums[left], nums[e] = nums[e], nums[left]

        self.qsh(s, left-1, nums)
        self.qsh(left+1, e, nums)

        return

        