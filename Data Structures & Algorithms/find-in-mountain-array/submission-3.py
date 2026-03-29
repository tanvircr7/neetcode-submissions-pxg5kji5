class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # find max index
        s = mountainArr.length()
        l,r = 0, s-1
        peak = 0
        while l<=r:
            m = l+(r-l)//2
            before = mountainArr.get(m-1)
            after = mountainArr.get(m+1)
            val = mountainArr.get(m)
            if before < val and after < val:
                peak = m
                break
            elif before < val and val < after:
                l = m+1
            else:
                r = m-1
        
        l,r = 0, peak
        while l<=r:
            m = l+(r-l) // 2
            val = mountainArr.get(m)
            if val==target:
                return m
            elif val < target:
                l = m+1
            else:
                r = m-1
        l,r = peak+1, s-1
        while l<=r:
            m = l+(r-l)//2
            val = mountainArr.get(m)
            if val == target:
                return m
            elif val < target:
                r = m-1
            else:
                l = m+1
        return -1