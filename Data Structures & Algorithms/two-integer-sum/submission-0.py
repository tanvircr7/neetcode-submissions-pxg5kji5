class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            val = target - n
            if val in prevMap:
                return [prevMap[val], i]
            prevMap[n] = i
        return []
                    