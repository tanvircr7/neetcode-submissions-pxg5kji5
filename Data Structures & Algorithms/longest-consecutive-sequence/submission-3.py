class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        count = {}

        for n in nums:
            count[n] = count.get(n,0)+1
        
        ans = 0

        for n in nums:
            if n-1 not in count:
                tmp = 1
                val = n+1

                while val in count:
                    val += 1
                    tmp += 1
                ans = max(ans, tmp)
        
        return ans
        