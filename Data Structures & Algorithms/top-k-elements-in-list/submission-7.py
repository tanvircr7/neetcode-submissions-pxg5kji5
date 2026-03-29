class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}

        for n in nums:
            cnt[n] = cnt.get(n,0)+1
        
        freq = {i:[] for i in range(1, len(nums)+1)}

        for key,v in cnt.items():
            freq[v].append(key)
    
        print(freq)

        res = []
        club = 0
        for i in range(len(nums), 0, -1):
            print(i)
            for x in freq[i]:
                print(f"insert {x}")
                if club == k:
                    return res
                res.append(x)
                club += 1
                print(f"{len(res)} - {club}")
        
        return res


