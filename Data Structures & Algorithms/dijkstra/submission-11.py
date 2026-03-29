class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {i: [] for i in range(n)}

        for x,y,z in edges:
            adj[x].append((y,z))

        hp = [[0,src]]
        shortest = {}

        while hp:
            w, u = heapq.heappop(hp)

            if u in shortest:
                continue
            
            shortest[u] = w

            for v, dw in adj[u]:
                if v not in shortest:
                    heapq.heappush(hp, (w+dw, v))
            
        
        for x in range(n):
            if x not in shortest:
                shortest[x]=-1
        
        return shortest