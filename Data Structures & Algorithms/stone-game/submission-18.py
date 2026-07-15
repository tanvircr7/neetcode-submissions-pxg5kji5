class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        def f(l,r):
            if l>r:
                return 0 
            
            if (l,r) in memo:
                return memo[(l,r)]
            
            even = (r-l+1) % 2 == 0
            takef = piles[l] if even else 0
            takel = piles[r] if even else 0

            first = takef + f(l+1,r)
            last = takel + f(l,r-1)
            res = max(first,last)
            memo[(l,r)] = res

            return res

        alice = f(0, len(piles)-1)
        bob = sum(piles) - alice

        return alice > bob