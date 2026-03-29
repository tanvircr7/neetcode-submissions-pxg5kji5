class Solution:
    def climbStairs(self, n: int) -> int:
        w = [-1]*n

        def f(i):
            if i==n:
                return 1            
            if i>n:
                return 0
            if w[i] != -1:
                return w[i]
                
            val = f(i+1)+f(i+2)
            w[i] = val
            return val

        return f(0)