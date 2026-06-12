class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        tmp = []

        def f(x,i):
            if i==len(s):
                if x==i:
                    res.append(tmp[:])
                return
                
            if self.isPali(s,x,i):
                tmp.append(s[x:i+1])
                f(i+1,i+1)
                tmp.pop()
            
            f(x,i+1)
            return

        f(0,0)
        return res
            
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True