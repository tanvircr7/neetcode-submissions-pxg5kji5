class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # find max index
        s = mountainArr.length()
        l,r = 0, s-1
        peak = 1
        while l<=r:
            m = l+(r-l)//2
            prev = mountainArr.get(m-1)
            x = mountainArr.get(m)
            after = mountainArr.get(m+1)
            if prev<x and x>after:
                peak = m
                break
            elif prev<x and x<after:
                l = m+1
            else:
                r = m-1
        l,r = 0, peak
        ans = -1
        while l<=r:
            m = l+(r-l)//2
            x = mountainArr.get(m)
            if x < target:
                l = m+1
            elif x > target:
                r = m-1
            else:
                ans = m
                break
        if ans != -1 : return ans
        l,r = peak+1, s-1
        while l<=r:
            m = l+(r-l)//2
            x = mountainArr.get(m)
            if x < target:
                r = m-1
            elif x > target:
                l = m+1
            else:
                ans = m
                break
        return ans