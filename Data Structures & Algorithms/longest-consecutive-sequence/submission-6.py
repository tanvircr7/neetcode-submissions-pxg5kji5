class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        
        cnt = {}
        for n in nums:
            cnt[n] = cnt.get(n,0)+1
        
        ans = 0
        for n in nums:
            if n-1 not in cnt:
                i=n
                tmp=0
                while i in cnt:
                    i+=1
                    tmp+=1
                ans = max(ans, tmp)
        
        return ans
