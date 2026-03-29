class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        seen = [0]*n

        for val in nums:
            if val>0 and val<=n:
                seen[val-1] = 1
        
        for i in range(1, n+1):
            if seen[i-1] == 0:
                return i
        
        return n+1

            
