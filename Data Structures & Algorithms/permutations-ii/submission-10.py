class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        tmp = []
        res = []

        nums.sort()

        cnt = {}
        for n in nums:
            cnt[n] = cnt.get(n,0)+1

        def f():
            if len(tmp)==len(nums):
                res.append(tmp[:])
                return
            
            for key, val in cnt.items():
                if cnt[key] > 0:
                    cnt[key] -= 1
                    tmp.append(key)
                    f()
                    tmp.pop()
                    cnt[key] += 1
        
        f()
        return res

