class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums)==1:
            return nums[0]

        def f(arr):
            memo = [-1]*len(arr)

            def rob(i):
                if i>=len(arr): return 0
                if memo[i] != -1:
                    return memo[i]
                steal = rob(i+2)+arr[i]
                nosteal = rob(i+1)
                v = max(steal, nosteal)
                memo[i] = v
                return v
            return rob(0)

        takefirst= f(nums[0:len(nums)-1])
        takelast = f(nums[1: ])

        return max(takefirst, takelast)