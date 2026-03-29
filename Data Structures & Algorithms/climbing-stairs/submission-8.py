class Solution:
    def climbStairs(self, n: int) -> int:
        w = [-1 for i in range(n+1)]
        
        def f(i):
            if i<0:
                return 0

            if w[i]!=-1:
                return w[i]
            
            if i==0 or i==1:
                return 1
            if i==2:
                return 2
            
            val = f(i-1)+f(i-2)
            w[i]=val
            return val
        
        return f(n)
