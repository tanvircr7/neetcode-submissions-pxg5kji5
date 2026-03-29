class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [-1 for i in range(50)]

        ways[0]=1
        ways[1]=1
        ways[2]=2

        def dp(i):

            if ways[i]!=-1:
                return ways[i]
            
            if i<0:
                return 0
            
            val = dp(i-1)+dp(i-2)

            ways[i] = val

            return val
        

        return dp(n)
