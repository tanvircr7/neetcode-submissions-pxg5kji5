class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {i: [] for i in range(n)}
        for x,y,z in edges:
            adj[x].append((y,z))
        
        pq = [[0, src]]
        shortest = {}

        while pq:
            d,u = heapq.heappop(pq)
            if u in shortest:
                continue
            
            shortest[u] = d

            for (v,dw) in adj[u]:
                if v not in shortest:
                    heapq.heappush(pq, (d+dw,v))
            
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        
        return shortest
