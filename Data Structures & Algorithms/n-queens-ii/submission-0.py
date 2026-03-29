class Solution:
    def totalNQueens(self, n: int) -> int:
        b = [["."]*n for _ in range(n)]
        res = []
        def f(row):

            if row==n:
                tmp = ["".join(x) for x in b]
                res.append(tmp[:])
                return
            
            for c in range(n):
                if self.isSafe(row, c, b):
                    b[row][c] = "Q"
                    f(row+1)
                    b[row][c] = "."
            
            return
        
        f(0)
        return len(res)

    def isSafe(self, row, col, b):
        r,c = row-1, col
        while r>=0:
            if b[r][c] == "Q":
                return False
            r-=1
        r,c = row-1, col-1
        while r>=0 and c>=0:
            if b[r][c] == "Q":
                return False
            r-=1
            c-=1
        r,c = row-1, col+1
        while r>=0 and c<len(b[0]):
            if b[r][c] == "Q":
                return False
            r-=1
            c+=1
        return True
