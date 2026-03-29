class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n=len(nums)
        target = n-k

        def partition(l,r):
            pivotIdx = r
            left = l
            for i in range(l,r):
                if nums[i]<=nums[pivotIdx]:
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1
            nums[left], nums[pivotIdx] = nums[pivotIdx], nums[left]
            return left
        
        l,r = 0, len(nums)-1
        pivot = len(nums)
        while pivot != target:
            pivot = partition(l,r)
            if pivot < target:
                l = pivot+1
            else:
                r = pivot-1
        return nums[target]

        
        # target = k-1

        # def partitionDescending(l,r):
        #     pivotIdx = r
        #     left = l
        #     for i in range(l,r):
        #         if nums[i] >= nums[pivotIdx]:
        #             nums[left], nums[i] = nums[i], nums[left]
        #             left += 1
        #     nums[left], nums[r] = nums[r], nums[left]
        #     return left
        

        # L, R = 0, len(nums)-1
        # pivot = 1000000
        
        # while pivot != target:
        #     pivot = partitionDescending(L,R)
        #     if pivot < target:
        #         L = pivot + 1
        #     else:
        #         R = pivot - 1
        
        # return nums[target]