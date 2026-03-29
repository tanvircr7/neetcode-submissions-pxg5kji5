class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        ans = nums[0]
        for n in nums:
            if curr < 0:
                curr = 0
            curr += n
            ans = max(curr, ans)
        
        return ans
            
        