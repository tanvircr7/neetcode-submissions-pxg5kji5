class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
            
        l=r=0
        curr = 0
        ans = len(nums)+1

        for r in range(len(nums)):
            curr += nums[r]

            while curr >= target:

                ans = min(ans, r-l+1)

                curr -= nums[l]
                l+=1
            
        
        return ans
