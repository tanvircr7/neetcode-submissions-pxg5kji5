class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        
        prefixSum = {0: 1}
        curr = 0

        for n in nums:
            curr += n

            diff = curr-k
            res += prefixSum.get(diff, 0)
            prefixSum[curr] = prefixSum.get(curr,0)+1
        
        return res