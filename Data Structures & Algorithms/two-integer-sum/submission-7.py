class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for j,n in enumerate(nums):
            diff = target-n

            if diff in prevMap:
                i = prevMap[diff]
                return [i,j]
            
            prevMap[n] = j
        
        return [0,0]
                

            

            
                    