class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        res = []

        def f(i):

            if i==len(nums):
                ans.append(res[:])
                return
            
            res.append(nums[i])
            f(i+1)
            res.remove(nums[i])

            f(i+1)

            return

        

        f(0)
        return ans