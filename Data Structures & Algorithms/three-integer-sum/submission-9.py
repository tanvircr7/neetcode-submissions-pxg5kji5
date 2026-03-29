class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            
            if n>0:
                break

            if i>0 and nums[i-1] == nums[i]:
                continue
            
            l=i+1
            r=len(nums)-1

            while l<r:
                val = n + nums[l] + nums[r]

                if val > 0:
                    r -= 1
                
                elif val < 0:
                    l += 1
                
                else:
                    res.append([n,nums[l], nums[r]])
                    
                    l += 1
                    r -= 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
        
        return res
