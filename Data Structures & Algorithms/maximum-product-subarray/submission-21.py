class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        p1, p2 = 1, 1

        for n in nums:
            tmp = p2
            p2 = max(p2*n, p1*n, n)
            p1 = min(p1*n, tmp*n, n)
            res = max(res, p2)
        
        return res