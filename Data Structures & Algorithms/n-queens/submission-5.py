class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        b = [["."]*n for i in range(n)]

        def dfs(i):
            if i==n:
                tmp = ["".join(r) for r in b]
                res.append(tmp.copy())
                return
            
            for col in range(n):
                if self.isSafe(b,i,col):
                    b[i][col] = "Q"
                    dfs(i+1)
                    b[i][col] = "."
        
        dfs(0)
        return res

    
    def isSafe(self, b, row, col):
        r,c = row-1, col
        while r>=0:
            if b[r][c]=="Q":
                return False
            r-=1
        r,c = row-1, col-1
        while r>=0 and c>=0:
            if b[r][c]=="Q":
                return False
            r-=1
            c-=1
        r,c = row-1, col+1
        while r>=0 and c<len(b[0]):
            if b[r][c]=="Q":
                return False
            r-=1
            c+=1
        return True
        
        