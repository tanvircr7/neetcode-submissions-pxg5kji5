class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}

        for n in nums:
            cnt[n] = cnt.get(n,0)+1
        print(cnt)
        
        mp = {i: [] for i in range(len(nums)+1)}
        for key, value in cnt.items():
            mp[value].append(key)

        print(mp)
        res = []
        for i in range(len(nums), 0, -1):
            for n in mp[i]:
                res.append(n)
                if len(res)==k:
                    return res
        
        return res

