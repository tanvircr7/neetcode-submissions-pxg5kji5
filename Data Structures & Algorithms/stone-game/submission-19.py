class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        
        def f(l,r):
            if l>r:
                return 0
            
            if (l,r) in memo:
                return memo[(l,r)]
            
            even = (r-l+1) % 2 == 0

            first = piles[l] if even else 0
            last = piles[r] if even else 0

            takef = f(l+1, r) + first
            takel = f(l,r-1) + last
            res = max(takef, takel)

            memo[(l,r)] = res
            return res
        
        alice = f(0, len(piles)-1)
        bob = sum(piles) - alice
        return alice > bob