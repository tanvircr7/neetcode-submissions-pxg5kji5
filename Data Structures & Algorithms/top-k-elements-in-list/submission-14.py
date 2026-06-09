class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}

        for n in nums:
            cnt[n] = cnt.get(n,0)+1
        
        freq = {i:[] for i in range(1, len(nums)+2)}

        for key,val in cnt.items():
            freq[val].append(key)
        print(freq)
        gg = []
        for i in range(len(nums)+1, 0, -1):
            
            for x in freq[i]:
                gg.append(x)
                if len(gg)==k:
                    return gg

        return gg