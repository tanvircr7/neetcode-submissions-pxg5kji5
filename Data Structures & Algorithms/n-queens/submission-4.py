class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        b = [["."]*n for i in range(n)]

        def backtrack(row):
            if row == n:
                tmp = ["".join(r) for r in b]
                res.append(tmp)
                return
            
            for c in range(n):
                if self.isSafe(row,c,b):
                    b[row][c] = "Q"
                    backtrack(row+1)
                    b[row][c] = "."
            
            return
        
        backtrack(0)
        return res

        
    def isSafe(self, row, col, b):
        r=row-1
        c=col
        while r>=0:
            if b[r][c]=="Q":
                return False
            r -= 1
        r=row-1
        c=col-1
        while r>=0 and c>=0:
            if b[r][c]=="Q":
                return False
            r-=1
            c-=1
        r=row-1
        c=col+1
        while r>=0 and c<len(b):
            if b[r][c]=="Q":
                return False
            r-=1
            c+=1
        return True
        
        