# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.msh(pairs, 0, len(pairs)-1)

    def msh(self, arr, s, e) -> List[Pair]:
        if e-s+1 <= 1:
            return arr
        
        mid = s + (e-s) // 2
        
        self.msh(arr, s, mid)
        self.msh(arr, mid+1, e)

        self.merge(arr, s, mid, e)

        return arr

    def merge(self, arr, s, mid, e):
        L = arr[s:mid+1]
        R = arr[mid+1:e+1]
        i = 0
        j = 0
        k = s

        while i<len(L) and j<len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                k += 1
                i += 1
            else:
                arr[k] = R[j]
                k += 1
                j += 1
            
        while i<len(L):
            arr[k] = L[i]
            k += 1
            i += 1

        while j<len(R):
            arr[k] = R[j]
            k += 1
            j += 1





        

    
