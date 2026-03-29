class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dp(i):
            if i>=len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dp(i+1)
            subset.pop()

            dp(i+1)

        dp(0)
        return res