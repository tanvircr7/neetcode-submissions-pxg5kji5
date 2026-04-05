class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def f(i, val):
            if i==len(nums):
                if val==0:
                    return 1
                return 0
            
            if (i,val) in memo:
                return memo[(i,val)]

            plus = f(i+1, val+nums[i])
            minus = f(i+1, val-nums[i])
            res = plus + minus
            
            memo[(i, val)] = res
            return res
        
        return f(0, target)