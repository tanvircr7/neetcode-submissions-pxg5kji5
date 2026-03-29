class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subsets = []

        def f(i):
            if i>=len(nums):
                ans.append(subsets[:])
                return
            
            subsets.append(nums[i])
            f(i+1)
            subsets.pop()

            f(i+1)


        
        f(0)

        return ans
        

