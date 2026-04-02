class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])

        l,r=0,m-1

        while l<=r:
            val = l+(r-l)//2

            if target<matrix[val][0]:
                r = val-1
            elif matrix[val][n-1]<target:
                l = val+1
            else:
                gg = matrix[val]
                x,y = 0, n-1

                while x<=y:
                    z = x+(y-x)//2

                    if gg[z] == target:
                        return True
                    elif gg[z] < target:
                        x = z+1
                    else:
                        y = z-1
                return False
        
        return False