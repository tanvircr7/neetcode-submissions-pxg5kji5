class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i,n in enumerate(nums):

            if n>0:
                break
            
            if i-1>=0 and nums[i-1]==nums[i]:
                continue

            l,r = i+1, len(nums)-1
            while l<r:
                val = nums[i]+nums[l]+nums[r]

                if val<0:
                    l+=1
                elif val>0:
                    r-=1
                else:
                    res.append([nums[i], nums[l], nums[r]])

                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    
                    l+=1
                    r-=1

        
        return res