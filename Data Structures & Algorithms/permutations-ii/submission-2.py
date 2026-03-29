class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []

        cnt = {i:0 for i in nums}

        for n in nums:
            cnt[n] = cnt.get(n,0)+1

        def dfs():
            if len(perm)==len(nums):
                res.append(perm.copy())
                return
            
            for n in cnt:
                if cnt[n]:
                    perm.append(n)
                    cnt[n] -= 1
                    dfs()
                    cnt[n] += 1
                    perm.pop()
        
        dfs()
        return res