class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def splitcnt(val):
            splits = 0
            currSum = 0
            for n in nums:
                currSum += n
                if currSum > val:
                    currSum = n
                    splits += 1
            return splits + 1
        
        l,r = max(nums), sum(nums)
        ans = r

        while l<=r:
            val = l+(r-l)//2

            cnt = splitcnt(val)

            if cnt <= k:
                r = val-1
                ans = val
            else:
                l = val+1
        
        return ans