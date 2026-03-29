class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums)==1:
            return nums[0]
        
        def dp(arr):
            memo = {}
            
            def dfs(i):
                if i in memo:
                    return memo[i]
                if i>=len(arr):
                    return 0
                memo[i] = max(arr[i]+dfs(i+2), dfs(i+1))
                return memo[i]
            
            return dfs(0)
        
        f = dp(nums[0: len(nums)-1])
        s = dp(nums[1: len(nums)])
            

        
        return max(f,s)
