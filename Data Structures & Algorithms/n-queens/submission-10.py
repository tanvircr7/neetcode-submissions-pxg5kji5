class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        b = [["."]*n for i in range(n)]

        def btrack(row):
            if row==n:
                tmp = ["".join(r) for r in b]
                res.append(tmp)
                return
            for col in range(n):
                if self.isSafe(b, row, col):
                    b[row][col] = "Q"
                    btrack(row+1)
                    b[row][col] = "."
            return
        btrack(0)
        return res

    def isSafe(self, b, r, c):
        row, col = r,c
        while row>=0:
            if b[row][col] == "Q":
                return False
            row -= 1

        row, col = r,c
        while row>=0 and col>=0:
            if b[row][col] == "Q":
                return False
            row-=1
            col-=1

        row, col = r,c
        while row>=0 and col<len(b[0]):
            if b[row][col] == "Q":
                return False
            row-=1
            col+=1
        return True
        
        
        