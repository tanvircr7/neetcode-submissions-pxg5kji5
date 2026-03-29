class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = [-1 for _ in range(len(nums))]


        def f(i):
            if i>=len(nums):
                return 0
                
            if memo[i] != -1:
                return memo[i]

            res = 0
            steal = f(i+2)+nums[i]
            nosteal = f(i+1)

            res = max(steal, nosteal)
            memo[i] = res
            return res

        return f(0)