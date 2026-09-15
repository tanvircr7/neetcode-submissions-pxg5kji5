class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        
        def subarrcnt(val):
            curr = 0
            partitions = 0
            for n in nums:
                curr += n
                if curr > val:
                    curr = n
                    partitions += 1
            return partitions + 1


        l,r = max(nums), sum(nums)
        res = r

        while l<=r:
            val = l+(r-l)//2

            cnt = subarrcnt(val)

            if cnt <= k:
                res = val
                r = val-1
            else:
                l = val+1
        
        return res
