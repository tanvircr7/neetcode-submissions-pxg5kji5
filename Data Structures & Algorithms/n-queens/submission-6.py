class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        b = [["."]*n for _ in range(n)]

        def f(row):
            if row==n:
                tmp = [''.join(r) for r in b]
                res.append(tmp.copy())
                return
            
            for c in range(n):
                if self.isSafe(b, row, c):
                    b[row][c] = "Q"
                    f(row+1)
                    b[row][c] = "."
        
        f(0)
        return res

    
    def isSafe(self, b, row, col):
        r,c = row, col
        while r>=0:
            if b[r][c]=="Q":
                return False
            r-=1
        r,c = row, col
        while r>=0 and c>=0:
            if b[r][c] == "Q":
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
        
        
        