class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        msk = matchsticks
        if sum(matchsticks)%4 != 0:
            return False
        
        sidelen = sum(msk)//4
        sides = [0]*4

        msk.sort(reverse=True)

        def dfs(i):
            if i==len(matchsticks):
                return True
            
            for side in range(4):

                if sides[side]+msk[i] <= sidelen:
                    sides[side] += msk[i]

                    if dfs(i+1):
                        return True
                    
                    sides[side] -= msk[i]
                
                if sides[side] == 0:
                    break
            
            return False
        
        return dfs(0)