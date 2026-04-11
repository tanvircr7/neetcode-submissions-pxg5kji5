class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def subarrCnt(val):
            currSum = 0
            splits = 0
            for n in nums:
                currSum += n
                if currSum > val:
                    currSum = n
                    splits += 1
            return splits+1
        
        l,r = max(nums), sum(nums)
        ans = max(nums)


        while l<=r:
            val = l+(r-l)//2

            subarrs = subarrCnt(val)

            if subarrs <= k:
                ans = val
                r = val-1
            else:
                l = val+1
        
        return ans