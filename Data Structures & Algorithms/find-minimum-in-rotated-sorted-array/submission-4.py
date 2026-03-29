class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1

        ans = 2000

        while l<=r:
            m = l+(r-l)//2

            if nums[m] <= nums[r]:
                # minimum element must be this one or something to its left
                r = m-1
                ans = min(ans, nums[m])
            else:
                # nums[m] > nums[r]
                # minimum element must be to the right
                l = m+1
        
        return ans
