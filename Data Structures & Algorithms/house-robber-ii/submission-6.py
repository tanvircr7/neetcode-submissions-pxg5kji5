class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums)==1:
            return nums[0]
        
        def f(arr):
            memo = {}

            def hrob(i):
                if i>=len(arr):
                    return 0
                
                if i in memo:
                    return memo[i]
                
                notrob = hrob(i+1)
                rob = hrob(i+2)+arr[i]
                res = max(notrob, rob)

                memo[i] = res
                return res
            
            return hrob(0)
        
        first = f(nums[:len(nums)-1])
        last = f(nums[1:])

        return max(first, last)