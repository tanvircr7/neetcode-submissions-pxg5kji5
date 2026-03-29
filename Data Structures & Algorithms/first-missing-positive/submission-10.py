class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        
        for i,n in enumerate(nums):
            if n<0:
                nums[i] = 0
        
        for i,n in enumerate(nums):
            val = abs(n)

            if 1<=val<=len(nums):

                if nums[val-1] > 0:
                    nums[val-1] *= -1
                
                elif nums[val-1] == 0:
                    nums[val-1] = (-1)*(len(nums)+1)

        
        for n in range(1, len(nums)+1):
            if nums[n-1] >= 0:
                return n
        
        return len(nums)+1
            
