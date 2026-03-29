class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        tmp = []
        ans = []

        def f(i,j):
            if i==0 and j==0:
                ans.append(tmp.copy())
                return
            
            if i==0:
                tmp.append(")")
                f(i,j-1)
                tmp.pop()
                return
            
            tmp.append("(")
            f(i-1, j)
            tmp.pop()

            if j-1 >= i:
                tmp.append(")")
                f(i,j-1)
                tmp.pop()
            
            return
        
        f(n,n)
        return ["".join(seq) for seq in ans]
