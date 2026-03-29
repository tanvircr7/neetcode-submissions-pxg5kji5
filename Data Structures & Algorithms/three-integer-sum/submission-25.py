class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            n = nums[i]
            if n>0:
                break
            
            if i-1 >= 0 and nums[i]==nums[i-1]:
                continue
            
            l,r= i+1, len(nums)-1
            while l<r:
                v = n+nums[l]+nums[r]
                if v > 0:
                    r -= 1
                elif v < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])

                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    
                    l+=1
                    r-=1
        
        return res