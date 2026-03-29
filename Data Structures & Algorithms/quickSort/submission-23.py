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
        if e-s+1 <= 1:
            return
        pivot = arr[e]
        left = s
        for i in range(s,e):
            if pairs[i].key < pivot.key:
                pairs[left],pairs[i] = pairs[i], pairs[left]
                left += 1
            
        pairs[left],pairs[e] = pairs[e], pairs[left]

        self.qsh(arr, s, left-1)
        self.qsh(arr, left+1, e)