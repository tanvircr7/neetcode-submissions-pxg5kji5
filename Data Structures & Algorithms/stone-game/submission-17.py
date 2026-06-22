class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        def f(l,r):
            if l>r:
                return 0
            
            if (l,r) in memo:
                return memo[(l,r)]

            even = (l-r+1) % 2 == 0
            takefirst = piles[l] if even else 0
            takelast = piles[r] if even else 0
            
            first = f(l+1, r)+takefirst
            last = f(l,r-1)+takelast
            res = max(first,last)
            memo[(l,r)] = res
            return res

        alice = f(0,len(piles)-1)
        bob = sum(piles) - alice

        return alice > bob