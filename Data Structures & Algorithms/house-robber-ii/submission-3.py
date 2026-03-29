class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums)==1:
            return nums[0]
        
        def func(tmpNums):
            memo = {}

            def f(i):
                if i>=len(tmpNums):
                    return 0
                    
                if i in memo:
                    return memo[i]
                
                steal = f(i+2)+tmpNums[i]
                nosteal = f(i+1)

                res = max(steal, nosteal)
                memo[i] = res
                return res
            
            return f(0)

        f = func(nums[0: len(nums)-1])
        s = func(nums[1: len(nums)])
        return max(f,s)
