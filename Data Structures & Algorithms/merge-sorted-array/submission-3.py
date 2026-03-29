class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i,j,k = 0,0,0
        tmp = nums1.copy()

        while i<m and j<n:
            print(f"==={k} {i} {j}===")
            print(f"{tmp[i]} - {nums2[j]}")
            if tmp[i] <= nums2[j]:
                nums1[k] = tmp[i]
                print(f"iii up")
                i+=1
            else:
                nums1[k] = nums2[j]
                print(f"j up")
                j+=1
            print(nums1)

            k+=1
        
        while i<m:
            nums1[k] = tmp[i]
            k+=1
            i+=1
            print("i rounding it off")
        while j<n:
            nums1[k] = nums2[j]
            k+=1
            j+=1
            print("JJJ rounding it off")


        
