class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            if target-n in prevMap:
                l = prevMap[target-n]
                return [l,i]
            
            prevMap[n] = i
        
        return [0,0]
                

            

            
                    