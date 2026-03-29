class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        tmp = []
        res = []

        cnt = {}
        for n in nums:
            cnt[n] = cnt.get(n,0)+1
        
        def dfs():
            if len(tmp)==len(nums):
                res.append(tmp.copy())
                return
            
            for key, value in cnt.items():
                if cnt[key] > 0:
                    tmp.append(key)
                    cnt[key]-=1
                    dfs()
                    cnt[key]+=1
                    tmp.pop()
            return
        
        dfs()
        return res
