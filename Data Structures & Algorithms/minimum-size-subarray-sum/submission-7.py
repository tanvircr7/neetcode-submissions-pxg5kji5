class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        reslen=100000
        curr = 0

        for r in range(len(nums)):
            curr += nums[r]

            while curr>= target:
                if r-l+1 < reslen:
                    reslen = r-l+1
                getout = nums[l]
                curr -= nums[l]
                l+=1
        
        return reslen if reslen != 100000 else 0