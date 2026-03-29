class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        
        l,r = 0, rows-1

        while l<=r:
            m = l+(r-l) // 2

            if target < matrix[m][0]:
                r = m-1
            elif target > matrix[m][cols-1]:
                l = m+1
            else:
                i,j = 0, cols-1

                while i<=j:
                    x = i+(j-i) // 2

                    curr = matrix[m]

                    if curr[x] < target:
                        i = x+1
                    elif curr[x] > target:
                        j = x-1
                    else:
                        return True
                
                return False
        
        return False