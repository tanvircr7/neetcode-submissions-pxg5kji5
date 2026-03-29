class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0

        cnt = {}
        for n in nums:
            cnt[n] = cnt.get(n,0)+1
        
        res = 0
        for n in nums:
            if n-1 not in cnt:
                tmp = 1
                val = n+1
                while val in cnt:
                    val += 1
                    tmp += 1
                res = max(res, tmp)
        
        return res