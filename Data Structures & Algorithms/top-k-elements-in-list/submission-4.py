class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}

        for n in nums:
            cnt[n] = cnt.get(n,0)+1
        
        freq = {i: [] for i in range(len(nums)+1)}

        for i,n in cnt.items():
            freq[n].append(i)
        
        res = []
        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) >= k:
                    return res
        
        return res
