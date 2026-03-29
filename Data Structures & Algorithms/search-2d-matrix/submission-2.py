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
                # row exists but is value present?
                x,y = 0, cols-1
                while x<=y:
                    z = x+(y-x)//2
                    if matrix[mid][z] > target:
                        y = z - 1
                    elif matrix[mid][z] < target:
                        x = z + 1
                    else:
                        return True
                return False
        
        return False                             # no row contains the target