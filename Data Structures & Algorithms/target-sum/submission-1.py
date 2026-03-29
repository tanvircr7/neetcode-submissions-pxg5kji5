class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}

        def f(i, val):
            if i==len(nums):
                if val==0:
                    return 1
                else:
                    return 0
            
            if (i,val) in memo:
                return memo[(i,val)]
            
            res = 0
            res += f(i+1, val+nums[i])
            res += f(i+1, val-nums[i])
            
            memo[(i,val)] = res

            return res
        
        return f(0, target)