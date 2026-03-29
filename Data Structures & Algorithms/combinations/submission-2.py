class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        subset = []

        def f(i):
            if len(subset) == k:
                res.append(subset[:])
                return
            
            if i>n:
                return
            
            subset.append(i)
            f(i+1)
            subset.pop()

            f(i+1)
            return 

            
        
        f(1)
        return res

        

