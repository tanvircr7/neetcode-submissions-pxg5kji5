class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        
        target = sum(nums) // 2
        n = len(nums)
        memo = {}

        def f(i, target):
            if target == 0:
                return True
            
            if i>=len(nums):
                return False
            
            if (i,target) in memo:
                return memo[(i,target)]

            notake = f(i+1, target)
            take = False
            if target-nums[i]>=0:
                take = f(i+1, target-nums[i])
            
            memo[(i, target)] = notake or take
            return memo[(i,target)]


        
        f(0, target)

        return memo[(0,target)]