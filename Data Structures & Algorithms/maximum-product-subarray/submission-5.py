class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin = 1, 1
        res = nums[0]

        for n in nums:
            if n == 0:
                currMin, currMax = 1, 1
            

            tmp = currMax
            currMax = max(currMax*n, currMin*n, n)
            currMin = min(tmp*n, currMin*n, n)
            res = max(currMax, res)


        return res


