class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        memo = {}
        nums = [1]+nums+[1]
        ans = 0


        def f(l,r):
            if l>r:
                return 0
            
            if (l,r) in memo:
                return memo[(l,r)]
            
            memo[(l,r)] = 0
            for i in range(l,r+1):
                coins = nums[l-1] * nums[i] * nums[r+1]
                coins += f(l,i-1) + f(i+1, r)
                memo[(l,r)] = max(memo[(l,r)], coins)
            
            return memo[(l,r)]
        
        return f(1, len(nums)-2)