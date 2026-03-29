class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}


        def alicepoints(l,r):
            if l>r:
                return 0
            
            if (l,r) in memo:
                return memo[(l,r)]

            even = (r-l+1)%2 == 0
            first = piles[l] if even else 0
            last = piles[r] if even else 0

            takefirst = alicepoints(l+1,r)+first
            takelast = alicepoints(l,r-1)+last

            memo[(l,r)] = max(takefirst, takelast)

            return max(takefirst, takelast)
        
        alice = alicepoints(0, len(piles)-1)
        total = sum(piles)

        return (total-alice) < alice