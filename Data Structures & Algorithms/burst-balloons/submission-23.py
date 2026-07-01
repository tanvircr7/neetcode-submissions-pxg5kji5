class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n=len(nums)
        xnums = [1]+nums+[1]

        dp = [[-1]*len(xnums) for _ in range(len(xnums))]
        memo = {}

        def f(l,r):
            if l>r:
                return 0
            
            if (l,r) in memo:
                return memo[(l,r)]
            
            memo[(l,r)] = 0
            for i in range(l,r+1):
                coins = xnums[l-1]*xnums[i]*xnums[r+1]
                coins += f(l,i-1) + f(i+1, r)
                memo[(l,r)] = max(memo[(l,r)], coins)
            
            return memo[(l,r)]
        
        return f(1, len(xnums)-2)