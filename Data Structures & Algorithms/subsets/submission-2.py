class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dp(i):
            print(f"-- {i} --")
            if i>=len(nums):
                res.append(subset.copy())
                return
            
            # take it
            subset.append(nums[i])
            dp(i+1)
            subset.remove(nums[i])
            # not take it
    
            dp(i+1)

        dp(0)
        return res