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
                    # After finding a match
                    res.append([n, nums[l], nums[r]])

                    # Skip all duplicates of nums[l]
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    # Skip all duplicates of nums[r]
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1

                    # Then move to next distinct pair
                    l += 1
                    r -= 1
        
        return res
