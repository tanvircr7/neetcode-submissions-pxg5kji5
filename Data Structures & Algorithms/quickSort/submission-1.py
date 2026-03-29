# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.qsh(pairs, 0, len(pairs)-1)
        return pairs

    def qsh(self, arr: List[Pair], s: int, e: int) -> None:
        if e - s + 1 <= 1:
            return
        
        pivot = arr[e]
        left = s

        for i in range(s, e):
            if arr[i].key < pivot.key:
                tmp = arr[i]
                arr[i] = arr[left]
                arr[left] = tmp
                left += 1
        
        arr[left], arr[e] = arr[e], arr[left]

        self.qsh(arr, s, left-1)
        self.qsh(arr, left+1, e)

        