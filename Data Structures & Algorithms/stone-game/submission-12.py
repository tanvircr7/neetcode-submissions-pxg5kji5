class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        def alice(l,r):
            if l>r:
                return 0
            
            if (l,r) in memo:
                return memo[(l,r)]
            
            even = (r-l+1) % 2 == 0
            takefirst = piles[l] if even else 0
            takelast = piles[r] if even else 0
            first = alice(l+1,r)+takefirst
            last = alice(l,r-1)+takelast
            res = max(first, last)
            memo[(l,r)] = res
            return res
        
        alicepoints = alice(0, len(piles)-1)
        bobpoints = sum(piles)-alicepoints
        
        return alicepoints > bobpoints