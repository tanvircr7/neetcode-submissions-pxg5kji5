class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0]*(2*len(nums))
        n = len(nums)

        for i, num in enumerate(nums):
            ans[i] = ans[i+n] = num
        return ans