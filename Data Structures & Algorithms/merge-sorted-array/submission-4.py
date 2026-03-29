class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i,j,k = m-1,n-1,m+n-1

        while i>=0 and j>=0:
            print(f"=={k} {i} {j}==")
            print(f"{nums1[i]}  -  {nums2[j]}")
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                print("i down")
                i-=1
            else:
                nums1[k] = nums2[j]
                print("j down")
                j-=1

            k-=1
        
        while i>=0:
            nums1[k] = nums1[i]
            k-=1
            i-=1

        while j>=0:
            nums1[k] = nums2[j]
            k-=1
            j-=1


        
