class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        
        def driver(arr):
            memo = {}

            def f(i):
                if i>=len(arr):
                    return 0
                
                if i in memo:
                    return memo[i]
                
                res = 0
                steal = f(i+2)+arr[i]
                nosteal = f(i+1)
                res = max(steal, nosteal)
                memo[i] = res

                return res
            
            return f(0)
        
        first = driver(nums[:len(nums)-1])
        last = driver(nums[1:])

        return max(first, last)