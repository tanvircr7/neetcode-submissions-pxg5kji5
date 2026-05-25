class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            val = abs(nums[i])

            if 1<=val<=n:
                if nums[val-1] > 0:
                    nums[val-1] *= -1
                
                elif nums[val-1] == 0:
                    nums[val-1] = -1*(n+1)
                

        for v in range(1, n+1):
            if nums[v-1] >= 0:
                return v
        
        return n+1

