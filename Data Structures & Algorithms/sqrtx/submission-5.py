class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0,x
        ans = 0
        while l<=r:
            m = l+(r-l)//2
            print(m)

            if m*m > x:
                r = m-1
            else:
                l = m+1
                ans = m
        
        return ans