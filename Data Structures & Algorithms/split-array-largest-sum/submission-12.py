class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def subarrCnt(val):
            currSum = 0
            splitcnt = 0
            for n in nums:
                currSum += n
                if currSum > val:
                    currSum = n
                    splitcnt += 1
            return splitcnt+1
        
        l,r = max(nums), sum(nums)
        ans = r

        while l<=r:
            val = l+(r-l)//2
            cnt = subarrCnt(val)

            if cnt <= k:
                ans = val
                r = val-1
            else:
                l = val+1
        
        return ans
