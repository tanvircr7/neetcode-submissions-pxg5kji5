class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        b = [["."]*n for _ in range(n)]

        def backtrack(r):
            if r==n:
                bcopy = ["".join(row) for row in b]
                res.append(bcopy)
                return
            
            for i in range(n):
                if self.isSafe(r,i,b):
                    b[r][i] = "Q"
                    backtrack(r+1)
                    b[r][i] = "."

        backtrack(0)
        return res
        
    def isSafe(self, row, col, b):
        r = row-1
        c = col-1
        while r>=0 and c>=0:
            if b[r][c]=="Q":
                return False
            r-=1
            c-=1
        r = row-1
        c = col
        while r>=0 and c>=0:
            if b[r][c]=="Q":
                return False
            r-=1
        r = row-1
        c = col+1
        while r>=0 and c<len(b):
            if b[r][c]=="Q":
                return False
            r-=1
            c+=1
        return True