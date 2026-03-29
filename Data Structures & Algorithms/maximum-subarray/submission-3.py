class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ans = nums[0]
        curr = 0
        for n in nums:
            if curr < 0:
                curr = 0
            curr += n
            ans = max(curr, ans)
        return ans
