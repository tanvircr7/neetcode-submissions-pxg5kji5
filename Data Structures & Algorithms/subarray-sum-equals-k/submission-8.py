class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixCnt = {0: 1}
        currSum = 0

        for n in nums:
            currSum += n
            
            diff = currSum - k

            res += prefixCnt.get(diff, 0)

            prefixCnt[currSum] = prefixCnt.get(currSum, 0)+1
        
        return res