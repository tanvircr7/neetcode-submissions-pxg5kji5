class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # find max index
        s = mountainArr.length()
        maxval,maxidx=0,0
        l,r=0,s-1
        while l<=r:
            m = l+(r-l)//2
            before = mountainArr.get(m-1)
            after = mountainArr.get(m+1)
            val = mountainArr.get(m)

            if before<val and val>after:
                maxval, maxidx = val, m
                break
            elif before<val and val<after:
                l = m+1
            else:
                r = m-1
        
        # check right
        l,r = 0, maxidx
        while l<=r:
            m = l+(r-l)//2
            val = mountainArr.get(m)
            if val<target:
                l = m+1
            elif val > target:
                r = m-1
            else:
                return m

        # check left
        l,r = maxidx+1, s-1
        while l<=r:
            m = l+(r-l)//2
            val = mountainArr.get(m)
            if val<target:
                r = m-1
            elif val > target:
                l = m+1
            else:
                return m
        return -1