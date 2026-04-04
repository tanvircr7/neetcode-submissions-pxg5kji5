class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 == 1:
            return False
        
        target = sum(nums)//2

        memo = {}

        def f(i, val):
            if val==0:
                return True
            
            if i>=len(nums):
                return False
            
            if (i,val) in memo:
                return memo[(i,val)]
            
            res = f(i+1, val)
            if val-nums[i]>=0:
                res = res or f(i+1, val-nums[i])

            memo[(i,val)] = res
            return res 
        
        return f(0, target)
