class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        ans = 100000
        curr = 0

        for r in range(len(nums)):
            curr += nums[r]

            while curr >= target:
                ans = min(ans, r-l+1)
                curr -= nums[l]
                l+=1
            
        
        return ans if ans!=100000 else 0