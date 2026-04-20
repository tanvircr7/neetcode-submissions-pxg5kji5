class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2==1:
            return False
        
        target = sum(nums)//2

        memo = {}


        def f(i, val):
            if val == 0:
                return True
            if i==len(nums):
                return False
            
            if (i,val) in memo:
                return memo[(i,val)]

            take = False
            if val-nums[i]>=0:
                take = f(i+1, val-nums[i])
            notake = f(i+1, val)
            
            res = take or notake
            memo[(i,val)] = res

            return res
        
        return f(0, target)
            