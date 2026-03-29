class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sticks = matchsticks
        if sum(sticks) % 4 != 0:
            return False
        
        val = sum(sticks)//4
        sticks.sort(reverse=True)
        sides = [0]*4

        def f(i):
            if i==len(sticks):
                return True

            for side in range(4):

                if sides[side]+sticks[i] <= val:
                    sides[side] += sticks[i]

                    if f(i+1):
                        return True
                    
                    sides[side] -= sticks[i]
                
                if sides[side] == 0:
                    break
            
            return False
        
        return f(0)




