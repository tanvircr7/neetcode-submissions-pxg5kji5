class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def canSplit(val):
            currSum = 0
            partitionCnt = 0

            for n in nums:
                currSum += n
                if currSum > val:
                    currSum = n
                    partitionCnt += 1
            
            subarrays = partitionCnt + 1
            return subarrays <= k
        
        L,R = max(nums), sum(nums)
        val = 0
        ans = float("infinity")

        while L<=R:
            print(f"{L}-{R}")
            val = L+(R-L) // 2
            print(f"Val {val}")
            if canSplit(val):
                print("split")
                R = val - 1
                ans = min(ans, val)
            else:
                L = val + 1
        

        return ans
