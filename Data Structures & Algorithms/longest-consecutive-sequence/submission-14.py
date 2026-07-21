class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        
        cnt = set()
        for n in nums:
            cnt.add(n)
        
        res = 0

        for i, n in enumerate(nums):
            if n-1 not in cnt:
                v = n+1
                tmp = 1
                while v in cnt:
                    v+=1
                    tmp += 1
                
                res = max(res, tmp)
        
        return res
