class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = count.get(n,0)+1
        
        for n, f in count.items():
            freq[f].append(n)
        
        ans=[]
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans)==k:
                    return ans
        
        return ans