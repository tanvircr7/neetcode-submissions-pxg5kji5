class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        sqs = defaultdict(set)


        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == '.':
                    continue

                if val in rows[i]:
                    print("ro")
                    return False
                if val in cols[j]:
                    print("col")
                    return False
                if val in sqs[i//3, j//3]:
                    return False

                rows[i].add(val)
                cols[j].add(val)
                sqs[i//3,j//3].add(val)
        
        return True
