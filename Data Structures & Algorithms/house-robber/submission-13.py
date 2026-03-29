class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = [-1 for _ in range(len(nums))]


        def f(i):
            if i>=len(nums):
                return 0
            
            if memo[i] != -1:
                return memo[i]
            
            steal = nums[i]+f(i+2)
            nosteal = f(i+1)
            val = max(steal, nosteal)
            memo[i] = val

            return val
            
        return f(0)