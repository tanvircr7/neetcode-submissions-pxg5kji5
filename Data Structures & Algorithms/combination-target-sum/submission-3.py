class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dp(i,val):
            if val == 0:
                res.append(subset[:])
                return
            
            if i>=len(nums):
                return
            
            if val-nums[i] >= 0:
                subset.append(nums[i])
                dp(i, val-nums[i])
                subset.remove(nums[i])
            
            dp(i+1, val)

        dp(0, target)
        return res