class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        tmp = []


        def f(i):
            if i>= len(nums):
                res.append(tmp.copy())
                return
                
            
            tmp.append(nums[i])
            f(i+1)
            tmp.remove(nums[i])
            f(i+1)
        
        f(0)
            
        return res

