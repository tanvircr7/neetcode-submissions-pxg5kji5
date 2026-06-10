class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        
        def subarrcnt(val):
            curr = 0
            splits = 0
            for n in nums:
                curr += n
                if curr > val:
                    curr = n
                    splits += 1
            return splits + 1
        
        l,r = max(nums), sum(nums)
        res = max(nums)

        while l<=r:
            m = l+(r-l)//2

            cnt = subarrcnt(m)

            if cnt <= k:
                r = m-1
                res = m
            else:
                l = m+1
        
        return res