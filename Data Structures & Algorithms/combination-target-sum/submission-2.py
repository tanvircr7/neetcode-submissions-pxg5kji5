class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, val):
            if val == 0:
                res.append(subset.copy())
                return
            
            if i>=len(nums):
                return
            
            if val-nums[i]>=0:
                subset.append(nums[i])
                dfs(i, val-nums[i])
                subset.pop()
           
            dfs(i+1, val)

        dfs(0, target)
        return res