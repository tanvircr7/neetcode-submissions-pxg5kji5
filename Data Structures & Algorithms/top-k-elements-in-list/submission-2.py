class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = count.get(n,0)+1
        
        for num, val in count.items():
            freq[val].append(num)
        
        cnt = 0
        ans = []
        for i in range(len(nums), 0, -1):

            for n in freq[i]:
                ans.append(n)
                cnt += 1
                if cnt >= k:
                    return ans
        
        return ans