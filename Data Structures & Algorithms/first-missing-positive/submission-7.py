class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        exists = [False]*len(nums)

        for n in nums:
            if 1<=n<=len(nums):
                exists[n-1] = True
        
        for n in range(1,len(nums)+1):
            if exists[n-1] == False:
                return n
        
        return len(nums)+1
