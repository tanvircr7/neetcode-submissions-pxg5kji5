class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        s = mountainArr.length()
        l,r = 0, s-1
        peak = -1
        while l<=r:
            val = l+(r-l)//2

            before = mountainArr.get(val-1)
            x = mountainArr.get(val)
            after = mountainArr.get(val+1)

            if before<x>after:
                peak = val
                break
            elif before<x<after:
                l = val+1
            else:
                r = val-1
        print(peak)
        l,r = 0, peak
        while l<=r:
            val = l+(r-l)//2
            x = mountainArr.get(val)
            
            if x==target:
                return val
            elif x<target:
                l = val+1
            else:
                r = val-1
        print(peak)
        l,r = peak+1, s-1
        while l<=r:
            val = l+(r-l)//2
            x = mountainArr.get(val)
            if x==target:
                return val
            elif x<target:
                r = val-1
            else:
                l = val+1
        print(peak)
        return -1