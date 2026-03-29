class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        res = nums[0]

        while l<=r:
            m = l + (r-l) // 2
            res = min(res, nums[m], nums[l], nums[r])
            if nums[m] >= nums[l]:
                l = m+1
            else:
                r = m-1
            
        return res

