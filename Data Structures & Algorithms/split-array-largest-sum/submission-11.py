class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def splitCnt(val):
            currSum = 0
            splits = 0
            for n in nums:
                currSum += n
                if currSum > val:
                    currSum = n
                    splits += 1
            subarr = splits+1
            return subarr
        
        l,r = max(nums), sum(nums)
        res = max(nums)

        while l<=r:
            val = l+(r-l)//2
            cnt = splitCnt(val)

            if cnt<=k:
                res = val
                r = val-1
            else:
                l = val+1

        return res