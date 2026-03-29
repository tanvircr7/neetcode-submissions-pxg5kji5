class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def canSplit(val):
            partitionCnt = 0
            currSum = 0
            for n in nums:
                currSum += n
                if currSum > val:
                    currSum = n
                    partitionCnt += 1
            
            subarray = partitionCnt + 1
            return subarray <= k


        l,r = max(nums), sum(nums)
        ans = 0
        while l<=r:
            m = l+(r-l) // 2

            if canSplit(m):
                r=m-1
                ans = m
            else:
                l=m+1
        
        return ans