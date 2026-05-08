class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []

        for i in range(len(nums)):

            if nums[i] > 0:
                break
            
            if i>0 and nums[i-1]==nums[i]:
                continue
            
            v = nums[i]
            l,r = i+1, len(nums)-1
            while l<r:
                val = v+nums[l]+nums[r]
                
                if val<0:
                    l += 1
                elif val>0:
                    r-=1
                else:
                    ans.append([v,nums[l], nums[r]])

                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    
                    l+=1

        
        return ans