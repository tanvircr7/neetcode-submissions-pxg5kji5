class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        idx = {}
        val = 0

        for n in nums:
            idx[n] = idx.get(n, 0)+1
        
        for n in nums:

            if n-1 not in idx:
                curr = n
                tmp = 1
                while curr+1 in idx:
                    tmp += 1
                    curr += 1
                val = max(val, tmp)
        

        if not nums:
            return 0
        
        return val