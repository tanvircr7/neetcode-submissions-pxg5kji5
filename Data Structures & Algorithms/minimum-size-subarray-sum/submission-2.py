class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=r=0
        curr = 0
        ans = len(nums)+1

        while r<len(nums):
            curr += nums[r]

            while curr >= target:
                if r-l+1<ans:
                    ans = r-l+1

                getout = l
                curr -= nums[l]
                l+=1

            r+=1
        
        return ans if ans < len(nums)+1 else 0