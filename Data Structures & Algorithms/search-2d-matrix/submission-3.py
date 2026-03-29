class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        
        # ---------- 1-D binary search on the *logical* 0 … rows-1 ----------
        l, r = 0, rows - 1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[mid][cols-1]:
                l = mid+1
            elif target < matrix[mid][0]:
                r = mid-1
            else:
                # 2nd binary search
                i,j=0,cols-1
                arr = matrix[mid]
                while i<=j:
                    x = i + (j-i) // 2
                    if target > arr[x]:
                        i = x+1
                    elif target < arr[x]:
                        j = x-1
                    else:
                        return True
                return False
        
        return False                             # no row contains the target