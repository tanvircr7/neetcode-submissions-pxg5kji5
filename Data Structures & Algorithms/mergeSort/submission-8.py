# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.msh(pairs, 0, len(pairs)-1)
    
    def msh(self, arr, s, e):
        if e-s+1<=1:
            return arr
        
        mid = s + (e-s) // 2

        self.msh(arr, s, mid)
        self.msh(arr, mid+1, e)

        self.merge(arr, s, mid, e)

        return arr

    def merge(self, arr, s, m, e):
        L = arr[s: m+1]
        R = arr[m+1: e+1]
        i,j,k = 0,0,s
        while i<len(L) and j<len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i+= 1
                k += 1
            else:
                arr[k] = R[j]
                j+= 1
                k +=1
        while i<len(L):
            arr[k] = L[i]
            i+= 1
            k += 1
        while j<len(R):
            arr[k] = R[j]
            j+= 1
            k += 1


        

    
