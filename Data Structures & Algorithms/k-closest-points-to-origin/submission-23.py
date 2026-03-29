class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dis = lambda x: x[0]*x[0] + x[1]*x[1]

        def quickSelect(l,r):
            pivot_idx = r
            pivot = points[pivot_idx]
            pivot_dis = dis(pivot)
            left = l
            for i in range(l,r):
                if dis(points[i])<=pivot_dis:
                    points[left], points[i] = points[i], points[left]
                    left += 1
            points[left], points[pivot_idx] = points[pivot_idx], points[left]
            return left

        
        l,r = 0, len(points)-1
        pivot = len(points)

        while pivot!=k:

            pivot = quickSelect(l,r)

            if pivot<k:
                l=pivot+1
            else:
                r=pivot-1
        
        return points[:k]

