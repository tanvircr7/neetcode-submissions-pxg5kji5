class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.qsh(nums, 0, len(nums)-1)
        return nums
    
    def qsh(self, nums, l, r):

        if r-l+1 <= 1:
            return
        
        import random
        pivot = random.randint(l,r)
        nums[pivot], nums[r] = nums[r], nums[pivot]
        pivot = r
        left = l
        for i in range(l,r):
            if nums[i] <= nums[pivot]:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
        
        nums[left], nums[pivot] = nums[pivot], nums[left]
        self.qsh(nums, l, left-1)
        self.qsh(nums, left+1, r)
        return