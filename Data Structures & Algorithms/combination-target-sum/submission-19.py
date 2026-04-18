class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        tmp = []

        def f(i, val):
            if val==0:
                res.append(tmp.copy())
                return
            if val<0:
                return
            if i==len(nums):
                return
            
            tmp.append(nums[i])
            f(i, val-nums[i])
            tmp.pop()
        

            f(i+1, val)
        
        f(0, target)
        return res