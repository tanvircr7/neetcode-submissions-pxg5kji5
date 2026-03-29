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
            
            for n in cnt:
                if cnt[n]>0:
                    cnt[n] -= 1
                    tmp.append(n)
                    f()
                    tmp.pop()
                    cnt[n] += 1
        
        f()
        return res