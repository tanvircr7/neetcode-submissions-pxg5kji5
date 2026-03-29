class Solution:
    def climbStairs(self, n: int) -> int:
        w = [-1 for i in range(n)]
        
        def f(i):
            if i>=n:
                return i==n
            if w[i] != -1:
                return w[i]
            w[i] = f(i+1)+f(i+2)
            return w[i]
        
        return f(0)
