class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        nums = candidates
        nums.sort()
        
        ans = []
        subset = []
        
        def dp(i,val):
            if val == 0:
                ans.append(subset.copy())
                return
            
            if i>=len(nums):
                return
            
            if val-nums[i]>=0:
                subset.append(nums[i])
                dp(i+1, val-nums[i])
                subset.pop()
            
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i += 1
            
            dp(i+1, val)
        

        dp(0, target)
        return ans
