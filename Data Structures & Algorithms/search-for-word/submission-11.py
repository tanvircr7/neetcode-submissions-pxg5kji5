class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])

        def f(r,c,i):
            if i==len(word):
                return True
            
            if r<0 or c<0 or r>=R or c>=C or board[r][c]=="#" or board[r][c]!=word[i]:
                return False
            
            board[r][c] = "#"

            res = f(r+1,c,i+1) or f(r-1,c,i+1) or f(r,c+1,i+1) or f(r,c-1,i+1)

            board[r][c] = word[i]

            return res
        
        for r in range(R):
            for c in range(C):
                
                if f(r,c,0):
                    return True
        
        return False