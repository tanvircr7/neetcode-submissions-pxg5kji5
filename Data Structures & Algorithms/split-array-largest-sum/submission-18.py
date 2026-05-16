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
        ans = l

        while l<=r:
            val = l+(r-l)//2

            cnt = subarrcnt(val)

            if cnt <= k:
                ans = val
                r = val-1
            else:
                l = val+1
        
        return ans