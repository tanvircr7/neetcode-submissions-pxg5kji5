class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        tmp = []
        res = []


        def f(i,j):
            if i==0 and j==0:
                res.append(tmp[:])
                return
            
            if i==0:
                tmp.append(")")
                f(i,j-1)
                tmp.pop()
                return
            
            if i>0:
                tmp.append("(")
                f(i-1,j)
                tmp.pop()
            
            if j-1 >= i:
                tmp.append(")")
                f(i,j-1)
                tmp.pop()
            
        
        f(n,n)
        ans = ["".join(seq) for seq in res]
        return ans
