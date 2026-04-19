# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.qsh( 0, len(pairs)-1, pairs)
        return pairs
    
    def qsh(self, s, e, arr):
        if e-s+1 <= 1:
            return arr
        
        pivot = arr[e]
        left = s
        for i in range(s, e):
            if arr[i].key < pivot.key:
                arr[left], arr[i] = arr[i], arr[left]
                left += 1
            
        arr[left], arr[e] = arr[e], arr[left]
        
        self.qsh(s, left-1, arr)
        self.qsh(left+1, e, arr)

        return 