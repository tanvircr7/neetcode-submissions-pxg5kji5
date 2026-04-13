class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        msk = matchsticks
        if sum(matchsticks)%4 != 0:
            return False
        
        msk.sort(reverse=True)

        sidelen = sum(msk)//4
        sides = [0]*4

        def f(i):
            if i==len(msk):
                return True
            
            for side in range(4):

                if sides[side]+msk[i] <= sidelen:

                    sides[side] += msk[i]

                    if f(i+1):

                        return True
                    
                    sides[side] -= msk[i]
                
                if sides[side] == 0:
                    break
            
            return False
        
        return f(0)