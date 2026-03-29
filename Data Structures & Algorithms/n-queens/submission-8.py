class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        b = [["."]*n for i in range(n)]

        def bk(row):
            if row == n:
                tmp = ["".join(r) for r in b]
                res.append(tmp.copy())
                return
            
            for c in range(n):
                if self.issafe(b, row, c):
                    b[row][c] = "Q"
                    bk(row+1)
                    b[row][c] = "."

            return
        
        bk(0)
        return res
    
    
    def issafe(self, b, r, c):
        row, col = r, c
        while row>=0:
            if b[row][col] == "Q":
                return False
            row -= 1
        row, col = r, c
        while row>=0 and col>=0:
            if b[row][col] == "Q":
                return False
            row -= 1
            col -= 1
        row, col = r, c
        while row>=0 and col<len(b[0]):
            if b[row][col] == "Q":
                return False
            row -= 1
            col += 1
        return True
        
        