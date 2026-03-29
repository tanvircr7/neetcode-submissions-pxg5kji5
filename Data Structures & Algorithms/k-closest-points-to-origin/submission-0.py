class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = []
        for i, l in enumerate(points):
            x = l[0]
            y = l[1]
            dis = math.sqrt((x*x)+(y*y))
            heapq.heappush(hp, [dis, i])
        
        ans = []
        while k:
            dis, idx = heapq.heappop(hp)
            ans.append(points[idx])
            k -= 1
        return ans