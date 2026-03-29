class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        tmp = []


        def f(i):
            if len(tmp) == k:
                res.append(tmp[:])
                return
            
            if i>n:
                return
            
            tmp.append(i)
            f(i+1)
            tmp.pop()

            f(i+1)
        
        f(1)
        return res