class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def cansplit(base):
            curr =0 
            cnt = 0
            for n in nums:
                curr += n
                if curr>base:
                    curr = n
                    cnt += 1
            subarr = cnt+1
            return subarr <= k    

        l,r = max(nums), sum(nums)
        ans = sum(nums)

        while l<=r:
            val = l+(r-l)//2

            if cansplit(val):
                # <= k
                ans = min(ans, val)
                r = val-1
            else:
                l = val+1
        
        return ans
