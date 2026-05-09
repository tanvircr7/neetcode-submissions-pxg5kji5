class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        b = [["."]*n for i in range(n)]

        def btrack(row):
            if row==n:
                tmp = ["".join(r) for r in b]
                res.append(tmp[:])
                return
            
            for c in range(n):
                if self.issafe(row,c,b):
                    b[row][c] = "Q"
                    btrack(row+1)
                    b[row][c] = "."
            
            return
        
        btrack(0)
        return res

    def issafe(self, row, col, board):
        r,c = row, col
        while r>=0:
            if board[r][c] == "Q":
                return False
            r-=1
        r,c = row, col
        while r>=0 and c>=0:
            if board[r][c] == "Q":
                return False
            r-=1
            c-=1
        r,c = row, col
        while r>=0 and c<len(board[0]):
            if board[r][c] == "Q":
                return False
            r-=1
            c+=1
        return True
        
        