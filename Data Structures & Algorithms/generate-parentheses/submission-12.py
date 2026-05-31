class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        tmp = []


        def f(i,j):
            if i==n and j==n:
                res.append(tmp.copy())
                return
            
            if i==n:
                tmp.append(")")
                f(i,j+1)
                tmp.pop()
                return
            
            if i<n:
                tmp.append("(")
                f(i+1,j)
                tmp.pop()
            
            if j+1<=i:
                tmp.append(")")
                f(i,j+1)
                tmp.pop()
        
        f(0,0)

        ans = ["".join(seq) for seq in res]

        return ans