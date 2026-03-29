class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        
        cnt = {}
        for n in nums:
            cnt[n] = cnt.get(n,0)+1
        
        res = 0
        for i, n in enumerate(nums):
            if n-1 not in cnt:
                print(f"check for {n}")
                v = n
                tmp = 0
                while v in cnt:
                    v+=1
                    tmp+=1
                res = max(res, tmp)
        
        return res