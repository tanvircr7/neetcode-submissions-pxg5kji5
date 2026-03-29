class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = []

        dis = lambda x: x[0]*x[0] + x[1]*x[1]

        for p in points:
            val = dis(p)*-1
            heapq.heappush(hp, [val, p])
            if len(hp) > k:
                heapq.heappop(hp)    
        
        ans = []
        while k:
            _, p = heapq.heappop(hp)
            ans.append(p)
            k -= 1
        
        return ans