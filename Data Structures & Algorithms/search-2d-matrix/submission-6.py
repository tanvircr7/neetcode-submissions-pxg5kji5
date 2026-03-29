class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m = len(matrix), len(matrix[0])

        l,r=0,n-1


        while l<=r:
            gg = l+(r-l)//2

            if target < matrix[gg][0]:
                r = gg-1
            elif target > matrix[gg][m-1]:
                l = gg+1
            else:
                x,y = 0, m-1
                arr = matrix[gg]

                while x<=y:
                    z = x+(y-x)//2

                    if target < arr[z]:
                        y = z-1
                    elif target > arr[z]:
                        x = z+1
                    else:
                        return True
                
                return False
        

        return False