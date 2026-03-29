class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        cpy = nums1[:m]
        i,j,k = 0,0,0

        while i<len(cpy) and j<len(nums2):
            if cpy[i] <= nums2[j]:
                nums1[k] = cpy[i]
                k+=1
                i+=1
            else:
                nums1[k] = nums2[j]
                k+=1
                j+=1
        
        while i<len(cpy):
            nums1[k] = cpy[i]
            k+=1
            i+=1
        while j<len(nums2):
            nums1[k] = nums2[j]
            k+=1
            j+=1