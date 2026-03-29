class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        def alicePoints(l,r):
            if l>r:
                return 0
            
            if (l,r) in memo:
                return memo[(l,r)]

            even = (r-l+1)%2 == 0

            point1 = piles[l] if even else 0
            point2 = piles[r] if even else 0

            left = alicePoints(l+1,r)+point1
            right = alicePoints(l,r-1)+point2

            val = max(left, right)

            memo[(l,r)] = val
            return val
        
        alice = alicePoints(0, len(piles)-1)
        total = sum(piles)

        return (total-alice)<alice
