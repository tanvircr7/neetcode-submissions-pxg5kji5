class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = []
        subset = []

        def dp(i):
            print(f"- {i}")
            if i>=len(nums):
                res.append(subset.copy())
                return
            
            
            print(f" goin in {i}")
            subset.append(nums[i])
            dp(i+1)
            subset.pop()

            while i+1<len(nums) and nums[i]==nums[i+1]:
                print(i)
                i += 1

            dp(i+1)

        dp(0)

        return res