class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def canSplit(val):
            print(f"--{val}")
            currSum = 0
            partCnt = 0
            for n in nums:
                currSum += n
                if currSum > val:
                    currSum = n
                    partCnt += 1
            
            subarrCnt = partCnt + 1
            print(f" subarrcnt {subarrCnt}")
            return subarrCnt

        L,R = max(nums), sum(nums)
        ans = sum(nums)

        while L<=R:
            val = L+(R-L)//2
            k_cnt = canSplit(val)

            if k_cnt <= k:
                R = val-1
                ans = min(ans, val)
            else:
                L = val+1
        
        return ans

