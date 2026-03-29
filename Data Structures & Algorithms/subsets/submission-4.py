class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsets = []

        def dp(i):
            if i>=len(nums):
                res.append(subsets.copy())
                return
            
            subsets.append(nums[i])
            dp(i+1)
            subsets.pop()

            dp(i+1)
        
        dp(0)
        return res