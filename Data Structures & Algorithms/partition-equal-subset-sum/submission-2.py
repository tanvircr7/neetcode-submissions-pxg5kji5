class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        
        dp = {}

        def f(i, target):
            if (i,target) in dp:
                return dp[(i,target)]

            if target == 0:
                return True
            
            if i >= len(nums):
                return False
            
            take = f(i+1, target-nums[i])
            notake = f(i+1, target)
            
            dp[(i,target)] = take or notake
            return take or notake

        
        return f(0, sum(nums)//2)