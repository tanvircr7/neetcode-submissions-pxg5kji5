class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        MID = (len(A)+len(B)) // 2

        if len(A)>len(B):
            A,B = B,A
        
        l,r = 0, len(A)-1
        while True:
            i = l + (r-l)//2

            j = MID - i -2

            Aleft = A[i] if i>=0 else float('-infinity')
            Aright = A[i+1] if (i+1)<=len(A)-1 else float('infinity')
            Bleft = B[j] if j>=0 else float('-infinity')
            Bright = B[j+1] if (j+1)<=len(B)-1 else float('infinity')

            if Aleft <= Bright and Bleft <= Aright:
                if (len(A)+len(B))%2 == 0:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
                else:
                    return min(Aright, Bright)

            elif Aleft > Bright:
                r = i-1
            else:
                l = i+1
        
        return True

