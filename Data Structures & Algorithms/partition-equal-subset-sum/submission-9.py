class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2==1:
            return False
        
        val = sum(nums)//2

        memo = {}

        def f(i, target):
            if target == 0:
                return True
            if i>=len(nums):
                return False
            
            if (i,target) in memo:
                return memo[(i,target)]
            
            res = False
            notake = f(i+1, target)
            take = False
            if target - nums[i]>=0:
                take = f(i+1, target-nums[i])
            
            res = notake or take
            memo[(i,target)] = res

            return res
        
        return f(0, val)
