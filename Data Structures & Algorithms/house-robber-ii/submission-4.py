class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums)==1:
            return nums[0]

        def f(arr):
            memo = [-1]*(len(arr))

            def h(i):
                if i>=len(arr):
                    return 0
                
                if memo[i] != -1:
                    return memo[i]

                steal = h(i+2)+arr[i]
                nosteal = h(i+1)

                res = max(steal, nosteal)
                memo[i] = res
                return res
            
            return h(0)

        takefirst= f(nums[0:len(nums)-1])
        takelast = f(nums[1: ])

        return max(takefirst, takelast)