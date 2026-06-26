class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}

        for n in nums:
            cnt[n] = cnt.get(n,0)+1
        
        freq = {i: [] for i in range(1, len(nums)+1)}

        res = []
        for key,val in cnt.items():
            freq[val].append(key)
        print(freq)
        for i in range(len(nums), 0, -1):
            print(f"{i} - {freq[i]}")
            for tmp in freq[i]:
                res.append(tmp)
                if len(res)==k:
                    return res

        return res