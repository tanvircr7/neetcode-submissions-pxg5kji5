class Solution:
    def jump(self, nums: List[int]) -> int:
        l=r=0
        res = 0
        maxr= 0

        while r<len(nums)-1:
            

            for j in range(l,r+1):
                maxr= max(maxr, j+nums[j])
            
            l = r+1
            r = maxr
            res += 1
            
        return res