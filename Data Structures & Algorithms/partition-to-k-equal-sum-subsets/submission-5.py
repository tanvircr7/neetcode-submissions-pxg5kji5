class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        val = sum(nums)//k
        if val*k != sum(nums):
            return False
        
        partsize = val
        parts = [0]*k

        def f(i):
            if i==len(nums):
                return True
            
            for part in range(k):

                if parts[part] + nums[i] <= partsize:
                    parts[part] += nums[i]

                    if f(i+1):

                        return True
                    
                    parts[part] -= nums[i]
                
                if parts[part] == 0:
                    break
            
            return False
        
        return f(0)