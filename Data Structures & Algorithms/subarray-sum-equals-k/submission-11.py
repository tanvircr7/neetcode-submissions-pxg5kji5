class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixCnt = {0: 1}
        curr = 0

        for n in nums:
            curr += n
            
            diff = curr-k

            res += prefixCnt.get(diff, 0)

            prefixCnt[curr] = prefixCnt.get(curr, 0)+1
        
        return res