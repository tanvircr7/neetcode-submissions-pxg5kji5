class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr = nums[0]
        ans = nums[0]

        for n in nums[1:]:
            curr = curr+n
            
            ans = max(ans, curr, n)
            if curr < 0:
                curr = 0
        
        return ans


