class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def subarrcnt(val):
            currSum = 0
            splits = 0
            for n in nums:
                currSum += n
                if currSum > val:
                    currSum = n
                    splits +=1
            return splits + 1
            
        l, r = max(nums), sum(nums)
        ans = r

        while l<=r:
            m = l+(r-l)//2
            cnt = subarrcnt(m)

            if cnt <= k:
                ans = m
                r = m-1
            else:
                l = m+1
        
        return ans
