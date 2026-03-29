class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def canSplit(val):
            subarrSplitCnt = 0
            currSum = 0

            for n in nums:
                currSum += n
                if currSum > val:
                    subarrSplitCnt += 1
                    currSum = n
            subarrCnt = subarrSplitCnt + 1
            return subarrCnt <= k

        
        l, r= max(nums), sum(nums)
        ans = float("infinity")
        while l<=r:
            m = l + (r-l) // 2

            if canSplit(m):
                r = m-1
                ans = min(m, ans)
            else:
                l = m+1
        
        return ans