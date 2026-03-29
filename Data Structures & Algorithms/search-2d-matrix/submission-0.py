class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        
        # ---------- 1-D binary search on the *logical* 0 … rows-1 ----------
        l, r = 0, rows - 1
        while l <= r:
            mid = (l + r) // 2
            if target < matrix[mid][0]:          # too small for this row
                r = mid - 1
            elif target > matrix[mid][-1]:       # too large for this row
                l = mid + 1
            else:                                # inside this row’s range
                # ---------- standard 1-D binary search inside the row ----------
                row = matrix[mid]
                left, right = 0, cols - 1
                while left <= right:
                    m = (left + right) // 2
                    if row[m] < target:
                        left = m + 1
                    elif row[m] > target:
                        right = m - 1
                    else:
                        return True
                return False                     # row exists but value absent
        
        return False                             # no row contains the target