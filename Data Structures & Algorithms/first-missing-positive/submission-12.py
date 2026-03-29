class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i] = 0

        n = len(nums)
        for i in range(n):
            val = abs(nums[i])

            if 1<=val<=n:
                if nums[val-1] > 0:
                    nums[val-1] = -1*nums[val-1]

                elif nums[val-1] == 0:
                    nums[val-1] = -1*(n+1)

        for i in range(1,n+1):
            if nums[i-1] >= 0:
                return i
        return n+1

            
