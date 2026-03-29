class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize 9 empty sets for each category
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        sqs = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                v = board[i][j]

                if v==".":
                    continue
                
                idx = (i//3)*3 + (j//3)
                if v in rows[i] or v in cols[j] or v in sqs[idx]:
                    return False
                
                rows[i].add(v)
                cols[j].add(v)
                sqs[idx].add(v)
        
        return True
