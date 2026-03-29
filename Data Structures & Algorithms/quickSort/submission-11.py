# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.qsh(pairs, 0, len(pairs)-1)
        return pairs

    def qsh(self, arr, s, e):
        if e-s+1 <=1:
            return
        
        pivot = arr[e]
        j = s

        for i in range(s,e):
            if arr[i].key < pivot.key:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
        
        arr[e], arr[j] = arr[j], arr[e]

        self.qsh(arr, s, j-1)
        self.qsh(arr, j+1, e)

        
        
