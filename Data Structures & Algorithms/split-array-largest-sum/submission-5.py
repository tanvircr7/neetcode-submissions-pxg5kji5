class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def canSplit(val):
            currSum = 0
            divs = 0
            for n in nums:
                currSum += n
                if currSum > val:
                    currSum = n
                    divs += 1
            subarrayCnt = divs+1
            return subarrayCnt

        
        L,R = max(nums), sum(nums)
        ans = L

        while L<=R:
            val = L+(R-L) // 2

            splits = canSplit(val)

            if splits<=k:
                R = val-1
                ans = val
            else:
                L = val+1
        
        return ans