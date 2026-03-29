class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dis = lambda x: x[0]*x[0] + x[1]*x[1]

        def quickSelect(l,r):
            pivotIdx = r
            pivotDis = dis(points[pivotIdx])
            left = l
            
            for i in range(l,r):
                if dis(points[i]) <= pivotDis:
                    points[left], points[i] = points[i], points[left]
                    left += 1
                    
            points[left], points[r] = points[r], points[left]
            return left
        
        L,R = 0, len(points)-1
        pivot = len(points)

        while pivot != k:
            pivot = quickSelect(L,R)
            
            if pivot < k:
                L = pivot + 1
            elif pivot > k:
                R = pivot - 1
            else:
                break
        
        return points[:k]