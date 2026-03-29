class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = [-1 for i in range(len(nums))]

        def f(i):
            
            if i<0:
                return 0

            if memo[i]!=-1:
                return memo[i]
            
            steal = f(i-2)+nums[i]
            notSteal = f(i-1)
            val = max(steal, notSteal)
            memo[i] = val
            return val
        
        return f(len(nums)-1)