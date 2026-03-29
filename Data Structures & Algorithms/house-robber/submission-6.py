class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = [-1 for i in range(len(nums))]

        def dp(i):
            if memo[i]>0:
                return memo[i]
            if i<0:
                return 0
            if i==0:
                return nums[0]
            if i==1:
                return nums[1]
            if i==2:
                return nums[2]+nums[0]
            
            v1 = dp(i-2)
            v2 = dp(i-3)

            memo[i] = max(v1,v2) + nums[i]
            return memo[i]
        
        last = len(nums)-1
        last2 = last - 1

        v1 = dp(last)
        v2 = dp(last2)
        
        return max(v1,v2)

        