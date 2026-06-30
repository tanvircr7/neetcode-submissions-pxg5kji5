class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        b = [["."]*n for _ in range(n)]
        res = []

        def f(row):
            if row==n:
                tmp = ["".join(r) for r in b]
                res.append(tmp)
                return
            
            for c in range(n):
                if self.issafe(row,c,b):
                    b[row][c] = "Q"
                    f(row+1)
                    b[row][c] = "."
            return 
        
        f(0)
        return res
        
    def issafe(self, row, col, b):
        r,c = row, col
        while r>=0:
            if b[r][c]=="Q":
                return False
            r-=1
        r,c = row, col
        while r>=0 and c>=0:
            if b[r][c]=="Q":
                return False
            r-=1
            c-=1
        r,c = row, col
        while r>=0 and c<len(b[0]):
            if b[r][c]=="Q":
                return False
            r-=1
            c+=1
        return True


        