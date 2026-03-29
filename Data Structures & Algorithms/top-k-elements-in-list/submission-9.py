class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for n in nums:
            cnt[n] = cnt.get(n,0)+1
        freq = {i:[] for i in range(1, len(nums)+1)}
        print(freq)
        for key,value in cnt.items():
            freq[value].append(key)
        
        res = []
        for i in range(len(nums), 0, -1):
            for v in freq[i]:
                res.append(v)
                if len(res)==k:
                    return res
        
        return res