class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def cansplit(val):
            currSum = 0
            cnt = 0
            for n in nums:
                currSum += n
                if currSum > val:
                    currSum = n
                    cnt += 1
            subarr = cnt + 1
            return subarr
            
        l,r = max(nums), sum(nums)
        ans = r
        while l<=r:
            val = l+(r-l)//2

            if cansplit(val) <= k:
                r = val - 1
                ans = val
            else:
                l = val + 1
        
        return ans
