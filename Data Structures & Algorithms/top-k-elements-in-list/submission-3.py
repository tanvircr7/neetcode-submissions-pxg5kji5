class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        freq = {i:[] for i in range(1, len(nums)+1)}

        for n in nums:
            cnt[n] = cnt.get(n, 0)+1
        
        for n, cnt in cnt.items():
            freq[cnt].append(n)
        
        res = []
        for i in range(len(nums), 0, -1):
            
            for n in freq[i]:
                res.append(n)

                if len(res) == k:
                    return res
        
        return res