class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k != 0:
            return False
        
        nums.sort(reverse=True)

        partsum = sum(nums)//k
        parts = [0]*k

        def f(i):
            if i==len(nums):
                return True
            
            for p in range(k):
                if parts[p]+nums[i]<=partsum:
                    parts[p] += nums[i]
                    if f(i+1):
                        return True
                    parts[p] -= nums[i]
                
                if parts[p]==0:
                    break

            return False

        return f(0)