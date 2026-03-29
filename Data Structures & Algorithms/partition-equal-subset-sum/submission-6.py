class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        
        target = sum(nums) // 2
        n = len(nums)
        memo = {}

        def f(i, val):
            if val==0:
                return True
            if i>=n:
                return False
            
            if (i,val) in memo:
                return memo[(i,val)]
            
            res = f(i+1, val)
            if val-nums[i]>=0:
                res = res or f(i+1, val-nums[i])
            
            memo[(i,val)] = res
            return res
        
        return f(0, target)
