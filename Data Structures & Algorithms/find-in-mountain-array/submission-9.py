class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        s = mountainArr.length()
        l,r = 0, s-1
        peak = -1
        ans = -1
        while l<=r:
            m = l+(r-l)//2
            before = mountainArr.get(m-1)
            v = mountainArr.get(m)
            after = mountainArr.get(m+1)

            if before<v and v>after:
                peak = m
                break
            elif before<v and v<after:
                l = m+1
            else:
                r = m-1
        l,r = 0, peak
        while l<=r:
            m = l+(r-l)//2
            v = mountainArr.get(m)

            if v==target:
                return m
            elif v<target:
                l = m+1
            else:
                r = m-1
        l,r = peak+1, s-1
        while l<=r:
            m = l+(r-l)//2
            v = mountainArr.get(m)

            if v==target:
                return m
            elif v<target:
                r = m-1
            else:
                l = m+1
        return ans