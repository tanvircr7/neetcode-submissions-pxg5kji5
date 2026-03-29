class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # find max index
        s = mountainArr.length()
        peak, l,r = 0, 0, s-1
        while l<=r:
            m = l+(r-l) // 2
            b = mountainArr.get(m-1)
            a = mountainArr.get(m+1)
            x = mountainArr.get(m)
            if b<x and x>a:
                peak = m
                break
            elif b<x and x<a:
                l = m+1
            else:
                r = m-1
        print(f"Peak {peak}")
        l,r = 0, peak
        ans = -1
        while l<=r:
            m = l+(r-l)//2
            x = mountainArr.get(m)
            if x==target:
                ans = m
                break
            elif x<target:
                l = m+1
            else:
                r = m-1
        if ans != -1 : return ans
        l,r = peak+1, s-1
        while l<=r:
            m = l+(r-l)//2
            x = mountainArr.get(m)
            if x == target:
                ans = m
                break
            elif x<target:
                r = m-1
            else:
                l = m+1
        return ans