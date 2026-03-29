class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums)-k

        def partition(l,r):
            pivotIdx = r
            left = l
            for i in range(l,r):
                if nums[i] <= nums[pivotIdx]:
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
        
        return nums[target]