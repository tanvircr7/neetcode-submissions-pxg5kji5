class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        half = sum(nums)//2
        if half*2 < sum(nums): 
            print("first")
            return False

        memo = {}

        def f(i, val):
            if val==0:
                return True
            if i>=len(nums):
                return False
            
            if (i,val) in memo:
                return memo[(i,val)]
            
            res = f(i+1, val)
            if val-nums[i]>=0:
                res = res or f(i+1, val-nums[i])
            
            memo[(i,val)] = res
            return res
        
        
        res = f(0, half)
        print(memo)
        return res