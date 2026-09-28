class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        def alice(l,r):
            if l>r:
                return 0
            
            if (l,r) in memo:
                return memo[(l,r)]
            
            even = (r-l+1)%2 == 0
            leftpoint = piles[l] if even else 0
            rightpoint = piles[r] if even else 0

            res = alice(l+1, r)+leftpoint
            res = max(res, alice(l,r-1)+ rightpoint)

            memo[(l,r)] = res
            return res
        
        
        al = alice(0, len(piles)-1)
        bob = sum(piles)-al

        return al > bob