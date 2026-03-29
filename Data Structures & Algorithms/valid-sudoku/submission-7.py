class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize 9 empty sets for each category
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sqs = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                if val == ".":
                    continue
                
                idx = (r//3)*3 + (c//3)

                if val in rows[r] or val in cols[c] or val in sqs[idx]:
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                sqs[idx].add(val)
                
        
        return True