class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixSumCnt = {0: 1}
        currSum = 0
        for n in nums:
            currSum += n    
            diff = currSum - k

            res += prefixSumCnt.get(diff, 0)
            prefixSumCnt[currSum] = prefixSumCnt.get(currSum,0)+1
        
        return res