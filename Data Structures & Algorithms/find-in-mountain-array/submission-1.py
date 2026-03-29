class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # find max index
        s = mountainArr.length()
        maxval,maxid=0,0
        l,r=0,s-1
        while l<=r:
            m = l+(r-l)//2
            mid = mountainArr.get(m)
            val1=-1
            if m-1 >= 0: val1 = mountainArr.get(m-1)
            val2=-1
            if m+1 < s: val2 = mountainArr.get(m+1)

            if val1<mid and val2<mid:
                maxval = mid
                maxidx = m
                break
            elif val1<mid and mid<val2:
                l=m+1
            else:
                r=m-1
        print(f"MAX {maxidx} - {maxval}")
        l,r =0,maxidx
        ans = -1
        while l<=r:
            m = l+(r-l)//2
            val = mountainArr.get(m)
            if val==target:
                ans = m
                break
            elif val<target:
                l=m+1
            else:
                r=m-1
        if ans!=-1: return ans

        l,r=maxidx,s-1
        while l<=r:
            m = l+(r-l)//2
            val = mountainArr.get(m)
            if val==target:
                ans = m
                break
            elif val<target:
                r=m-1
            else:
                l=m+1
        return ans
        