class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclid = lambda x: x[0]*x[0] + x[1]*x[1]
        import random

        def partition(l, r):
            pivotIdx = random.randint(l, r)
            points[pivotIdx], points[r] = points[r], points[pivotIdx]
            pivotIdx = r
            pivotDis = euclid(points[pivotIdx])

            left = l
            for i in range(l,r):
                if euclid(points[i]) <= pivotDis:
                    points[left], points[i] = points[i], points[left]
                    left += 1
            points[left], points[r] = points[r], points[left]

            return left

        
        L, R = 0, len(points)-1
        pivot = len(points)

        while pivot != k:
            pivot = partition(L,R)

            if pivot < k:
                L = pivot + 1
            else:
                R = pivot -1
        
        return points[:k]