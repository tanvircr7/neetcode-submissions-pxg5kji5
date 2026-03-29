class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def canSplit(val):
            currSum = 0
            parts = 0
            for n in nums:
                currSum += n
                if currSum > val:
                    currSum = n
                    parts += 1
            return parts+1 <= k


        
        l,r = max(nums), sum(nums)
        ans = sum(nums)
        while l<=r:
            val = l+(r-l)//2

            if canSplit(val):
                r=val-1
                ans = val
            else:
                l=val+1
        
        return ans
