class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        res = False
        l,r = 0, m-1

        while l<=r:
            idx = l+(r-l)//2

            if target < matrix[idx][0]:
                r = idx-1
            elif target > matrix[idx][n-1]:
                l = idx+1
            else:
                arr = matrix[idx]
                x,y = 0, n-1
                while x<=y:
                    z = x+(y-x)//2

                    if arr[z]==target:
                        return True
                    elif arr[z]<target:
                        x = z+1
                    else:
                        y = z-1
                return False
        
        return False

