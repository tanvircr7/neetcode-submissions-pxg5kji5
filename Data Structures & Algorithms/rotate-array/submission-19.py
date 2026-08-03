class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)

        def rev(l,r):
            while l<r:
                nums[l],nums[r] = nums[r], nums[l]
                l+=1
                r-=1

        
        # tmp = [0]*len(nums)

        # for i in range(n):
        #     tmp[(i+k)%n] = nums[i]
        
        # nums[:] = tmp
        n = len(nums)
        rev(0, n-1)
        rev(0, k-1)
        rev(k, n-1)



