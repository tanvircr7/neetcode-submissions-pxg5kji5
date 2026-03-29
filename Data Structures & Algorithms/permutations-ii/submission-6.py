class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        tmp = []
        cnt = {}
        for n in nums:
            cnt[n] = cnt.get(n,0)+1
        
        def f():
            if len(tmp)==len(nums):
                res.append(tmp[:])
                return
            
            for k,v in cnt.items():
                if cnt[k] > 0:
                    tmp.append(k)
                    cnt[k] -= 1
                    f()
                    cnt[k] += 1
                    tmp.pop()
        
        f()
        return res
