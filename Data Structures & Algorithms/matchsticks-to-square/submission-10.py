class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False

        sides = [0]*4
        sidelen = sum(matchsticks)//4
        matchsticks.sort(reverse=True)

        def f(i):
            if i==len(matchsticks):
                return True
            
            for side in range(4):

                if sides[side]+matchsticks[i] <= sidelen:
                    sides[side] += matchsticks[i]
                    
                    if f(i+1):
                        return True
                    
                    sides[side] -= matchsticks[i]
                
                if sides[side] == 0:
                    break
            
            return False
        
        return f(0)