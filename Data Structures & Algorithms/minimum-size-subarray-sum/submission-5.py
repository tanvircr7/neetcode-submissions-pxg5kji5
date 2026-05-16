class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
            
        l=r=0
        reslen = len(nums)
        curr = 0

        for r in range(len(nums)):
            curr += nums[r]

            while curr >= target:
                if r-l+1 < reslen:
                    reslen = r-l+1
                curr -= nums[l]
                l+=1
            
        
        return reslen