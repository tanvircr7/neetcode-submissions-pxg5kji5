class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(list)
        rows = defaultdict(list)
        sqs = defaultdict(list)

        for i in range(len(board)):
            for j in range(len(board)):

                val = board[i][j]

                if val==".":
                    continue
                
                if val in rows[i] or val in cols[j] or val in sqs[i//3,j//3]:
                    return False
                
                rows[i].append(val)
                cols[j].append(val)
                sqs[i//3,j//3].append(val)
        
        return True