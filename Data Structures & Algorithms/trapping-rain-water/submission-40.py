class Solution:
    def trap(self, h: List[int]) -> int:
        res = 0
        minL, minR = h[0], h[len(h)-1]
        l=0
        r=len(h)-1

        while l<=r:
            
            if minL<minR:
                tmp = minL-h[l]
                print(tmp)
                res += max(0, tmp)
                minL = max(minL, h[l])
                l+=1
            else:
                tmp = minR-h[r]
                print(tmp)
                res += max(0, tmp)
                minR = max(minR, h[r])
                r-=1
        
        return res
        
        