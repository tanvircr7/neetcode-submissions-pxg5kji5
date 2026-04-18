class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        tmp = []
        res = []

        def f(i):
            if i==len(nums):
                res.append(tmp[:])
                return
            
            tmp.append(nums[i])
            f(i+1)
            tmp.pop()

            f(i+1)
        
        f(0)
        return res