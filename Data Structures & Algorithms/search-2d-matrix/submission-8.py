class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])

        l,r=0,m-1

        while l<=r:
            mid=l+(r-l)//2
            
            if matrix[mid][0]>target:
                r =mid-1
            elif matrix[mid][n-1]<target:
                l = mid+1
            else:
                x,y=0,n-1
                val = matrix[mid]

                while x<=y:
                    z = x+(y-x)//2
                    if val[z] < target:
                        x = z+1
                    elif val[z] > target:
                        y = z-1
                    else:
                        return True

                return False

        return False