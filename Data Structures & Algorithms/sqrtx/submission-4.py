class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0,x
        ans = 0
        while l<=r:
            m = l+(r-l)//2
            print(m)

            if m*m <= x:
                ans=m
                l=m+1
            else:
                r=m-1
            print(f"{l} - {r}")
        
        return ans