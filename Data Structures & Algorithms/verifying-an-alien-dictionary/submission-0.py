class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_idx = {c: i for i, c in enumerate(order)}

        def compare(word):
            return [order_idx[c] for c in word]
        
        return words == sorted(words, key=compare)