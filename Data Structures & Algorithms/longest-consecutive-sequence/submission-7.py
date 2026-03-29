class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0

        cnt = {}
        for n in nums:
            cnt[n] = cnt.get(n,0)+1
        
        ans = 1
        for n in nums:
            if n-1 not in cnt:
                size = 1
                k = n+1
                while k in cnt:
                    k+=1
                    size+=1
                ans = max(ans, size)
        
        return ans