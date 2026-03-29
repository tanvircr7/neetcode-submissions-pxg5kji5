class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        nums.sort()

        res = []
        tmp = []

        def f(i, val):
            if val == 0:
                res.append(tmp.copy())
                return
            
            if i>=len(nums):
                return
            
            if val - nums[i] >= 0:
                tmp.append(nums[i])
                f(i+1, val-nums[i])
                tmp.pop()
                
            while i+1<len(nums) and nums[i] == nums[i+1]:
                    i += 1
            
            f(i+1, val)
        
        f(0, target)

        return res