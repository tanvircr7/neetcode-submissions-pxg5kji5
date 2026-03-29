class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i,n in enumerate(nums):
            deficit = target-n
            if deficit in prevMap:
                return [prevMap[deficit], i]
            prevMap[n] = i
        
        return [0,1]
            
                    