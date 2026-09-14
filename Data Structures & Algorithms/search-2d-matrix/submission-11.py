class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        res = False

        l,r = 0, m-1

        while l<=r:
            idx = l+(r-l)//2

            if target < matrix[idx][0]:
                r = idx-1
                print(f" -- {matrix[idx][0]} -- ")
            elif target > matrix[idx][n-1]:
                l = idx+1
                print(f" -- {matrix[idx][n-1]} -- ")
            else:
                print("dig")
                start, end = 0, n-1
                arr = matrix[idx]

                while start <= end:
                    y = start+(end-start)//2
                    print(f"-- arr {arr[y]} --")
                    if target < arr[y]:
                        end = y-1
                    elif target > arr[y]:
                        start = y+1
                    else:
                        return True

                return False

        return False    

