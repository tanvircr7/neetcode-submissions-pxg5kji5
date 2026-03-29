# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.msh(pairs, 0, len(pairs)-1)
    
    def msh(self, arr, l, r):
        if r-l+1 <= 1:
            return arr
        m = l+(r-l)//2
        self.msh(arr, l, m)
        self.msh(arr, m+1, r)
        self.merge(arr, l,m,r)
        return arr
    
    def merge(self, arr, l,m,r):
        L=arr[l:m+1]
        R=arr[m+1:r+1]
        i,j,k = 0,0,l

        while i<len(L) and j<len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        while i<len(L):
            arr[k] = L[i]
            k+=1
            i+=1
        while j<len(R):
            arr[k] = R[j]
            k+=1
            j+=1

