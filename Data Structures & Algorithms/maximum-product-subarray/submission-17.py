class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMax, currMin = 1, 1

        for n in nums:
            tmp = currMax

            currMax = max(currMax*n, currMin*n, n)
            currMin = min(tmp*n, currMin*n, n)

            res = max(res, currMax)
        
        return res