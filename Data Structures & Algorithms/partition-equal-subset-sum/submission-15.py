class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        target = total//2

        if total != target*2:
            return False
        memo = {}
        
        def f(i, val):
            if val==0:
                return True
            
            if i==len(nums):
                return False
            
            res = False
            if val-nums[i] >= 0:
                res = res or f(i+1, val-nums[i])
            res = res or f(i+1, val)

            memo[(i,val)] = res
            return res

        return f(0, target)