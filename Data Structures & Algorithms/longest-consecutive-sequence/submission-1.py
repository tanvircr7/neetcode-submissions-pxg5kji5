class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        idx = {}
        ans = -1
        if len(nums) == 0:
            return 0
        for n in nums:
            if n not in idx:
                idx[n] = 1
        
        for n in nums:
            if n-1 not in idx:
                curr = n
                val = 1
                while curr+1 in idx:
                    val +=1
                    curr +=1
                ans = max(ans, val)
        

        return ans