class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        nums.sort()

        res = []
        subset = []

        def f(i, val):
            if val == 0:
                res.append(subset[:])
                return
            if i>=len(nums):
                return
            
            if val-nums[i]>=0:
                subset.append(nums[i])
                f(i+1, val-nums[i])
                subset.pop()
            
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            
            f(i+1, val)
            return

        f(0, target)

        return res