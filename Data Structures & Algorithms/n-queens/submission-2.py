class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        b = [["."]*n for i in range(n)]
        
        def backtrack(r):
            if r==n:
                copy = ["".join(row) for row in b]
                res.append(copy)
                return
            
            for c in range(n):
                if self.isSafe(r,c,b):
                    b[r][c] = "Q"
                    backtrack(r+1)
                    b[r][c] = "."
        backtrack(0)
        return res

    def isSafe(self, r, c, b):
        # upper columns check
        row = r-1
        while row>=0:
            if b[row][c] == "Q":
                return False
            row -= 1
        # diagonal left
        row, col = r-1, c-1
        while row>=0 and col>=0:
            if b[row][col] == "Q":
                return False
            row -= 1
            col -= 1
        # diagonal right
        row, col = r-1, c+1
        while row>=0 and col<len(b):
            if b[row][col] == "Q":
                return False
            row -= 1
            col += 1
        # return 
        return True
        