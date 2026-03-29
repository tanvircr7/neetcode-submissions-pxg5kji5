class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        row, col = len(matrix), len(matrix[0])
        
        l,r=0,len(matrix)-1

        while l<=r:
            # print(f"{l} - {r}")
            m = l + (r-l) // 2

            if matrix[m][0] > target:
                r = m-1
            elif matrix[m][col-1] < target:
                l = m+1
            else:
                x,y = 0, col
                # print(f"GOT HIM {m}")
                while x<=y:
                    z = x+(y-x) // 2
                    val = matrix[m]

                    if val[z] > target:
                        y = z-1
                    elif val[z] < target:
                        x = z+1
                    else:
                        # print(f"-> {m}{z}")
                        return True
                
                return False
        
        return False