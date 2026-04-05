class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}


        def alicepoints(l,r):
            if l>r:
                return 0
            
            if (l,r) in memo:
                return memo[(l,r)]

            even = (r-l+1)%2 == 0

            firstval = piles[l] if even else 0
            lastval = piles[r] if even else 0

            takefirst = alicepoints(l+1,r)+firstval
            takelast = alicepoints(l,r-1)+lastval       
            res = max(takefirst, takelast)

            memo[(l,r)] = res
            return res
        
        alice = alicepoints(0, len(piles)-1)
        total = sum(piles)
        bob = total - alice
        return alice>bob