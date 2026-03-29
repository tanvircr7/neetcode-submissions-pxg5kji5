class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A)>len(B):
            A,B = B,A
        total = len(A)+len(B)
        half = total // 2
        l,r = 0, len(A)-1
        while True:
            i = l + (r-l)//2
            j = half-(i+1)-1

            Al = A[i] if i>=0 else float("-infinity")
            Ar = A[i+1] if i+1<len(A) else float("infinity")
            Bl = B[j] if j>=0 else float("-infinity")
            Br = B[j+1] if j+1<len(B) else float("infinity")

            if Al<=Br and Bl<=Ar:
                if total % 2:
                    return min(Ar,Br)
                else:
                    return (max(Al,Bl)+min(Ar,Br))/2.0
            elif Al>Br:
                r = i-1
            else:
                l = i+1
        
        return 1.0
            
