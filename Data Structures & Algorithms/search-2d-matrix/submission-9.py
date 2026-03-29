class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])

        l,r=0,m-1

        while l<=r:
            idx = l+(r-l)//2

            if target<matrix[idx][0]:
                r = idx-1
            elif target > matrix[idx][n-1]:
                l = idx+1
            else:
                x,y = 0, n-1
                val = matrix[idx]

                while x<=y:
                    z = x+(y-x)//2

                    if val[z] == target:
                        return True
                    elif val[z]<target:
                        x = z+1
                    else:
                        y = z-1

                return False

        return False 