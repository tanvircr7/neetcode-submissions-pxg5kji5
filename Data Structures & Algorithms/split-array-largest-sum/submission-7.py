class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def canSplit(val):
            currSum=0
            splitcnt=0
            for n in nums:
                currSum += n
                if currSum > val:
                    currSum = n
                    splitcnt += 1
            subarr_cnt = splitcnt+1
            return subarr_cnt<=k



        L,R = max(nums), sum(nums)
        ans = sum(nums)

        while L<=R:
            val = L+(R-L)//2
            print(f"{L} - {R} - val {val}")

            if canSplit(val):
                ans = min(ans, val)
                R=val-1
            else:
                L=val+1
            print(ans)

        return ans
