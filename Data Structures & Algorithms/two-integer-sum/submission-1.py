class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i in range(len(nums)):
            val = target - nums[i]
            if val in prevMap and i!=prevMap[val]:
                return [prevMap[val], i]
            prevMap[nums[i]]=i

        return [0,1]
                    