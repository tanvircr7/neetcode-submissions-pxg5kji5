class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        target = n-k

        dis = lambda x: x[0]*x[0] + x[1]*x[1]

        def partition(l,r):
            idx = r
            left = l
            for i in range(l,r):
                if nums[i] < nums[idx]:
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1
            nums[left], nums[r] = nums[r], nums[left]
            return left
        
        L, R = 0, len(nums)-1
        pivot = len(nums)
        
        while pivot != target:
            pivot = partition(L,R)
            if pivot < target:
                L = pivot + 1
            else:
                R = pivot - 1
        
        return nums[pivot]

        
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