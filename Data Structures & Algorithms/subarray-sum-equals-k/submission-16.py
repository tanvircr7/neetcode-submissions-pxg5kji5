class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixcnt = {0:1}
        curr = 0

        for n in nums:
            curr += n
            diff = curr-k

            res += prefixcnt.get(diff, 0)
            prefixcnt[curr] = prefixcnt.get(curr, 0)+1

        return res