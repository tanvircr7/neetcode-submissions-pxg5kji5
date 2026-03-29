class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        def alicePoints(l,r):
            if l>r:
                return 0
            
            if (l,r) in memo:
                return memo[(l,r)]

            even = (r-l+1) % 2 == 0
            
            left = piles[l] if even else 0
            right = piles[r] if even else 0

            takeleft = alicePoints(l+1, r) + left
            takeright = alicePoints(l,r-1) + right

            memo[(l,r)] = max(takeleft, takeright)
            return memo[(l,r)]
            
        alice = alicePoints(0, len(piles)-1)
        total = sum(piles)

        return (total-alice)<alice
