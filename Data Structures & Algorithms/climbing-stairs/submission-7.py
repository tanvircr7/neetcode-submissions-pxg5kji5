class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [-1 for _ in range(n+1)]

        def f(i):
            if ways[i] != -1:
                return ways[i]

            if i==0 or i==1:
                return 1
            if i==2:
                return 2
            
            val = f(i-1)+f(i-2)
            ways[i] = val
            return val

        return f(n)