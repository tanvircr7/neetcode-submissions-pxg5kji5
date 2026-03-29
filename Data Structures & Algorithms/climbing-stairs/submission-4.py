class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [-1 for i in range(50)]
        ways[0]=1
        ways[1]=1
        ways[2]=2

        def f(i):

            if i<0:
                return 0

            if ways[i] != -1:
                return ways[i]
            
            ways[i] = f(i-1)+f(i-2)

            return ways[i]

        return f(n)