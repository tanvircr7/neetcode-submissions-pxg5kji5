class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}

        def dfs(index, val):
            
            if index == len(nums):
                if val==target:
                    return 1
                else:
                    return 0

            if (index, val) in memo:
                return memo[(index, val)]
            
            plus = dfs(index+1, val+nums[index])
            minus = dfs(index+1, val-nums[index])
            
            memo[(index, val)] = plus+minus

            return memo[(index, val)]
        

        val = dfs(0, 0)
        print(memo)
        
        return val
