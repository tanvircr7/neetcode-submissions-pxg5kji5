class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {i:[] for i in range(n)}

        for u,v,w in edges:
            adj[u].append((v,w))
        
        shortest = {}
        hp = [(0, src)]

        while hp:
            w, v = heapq.heappop(hp)

            if v in shortest:
                continue
            
            shortest[v] = w

            for u, dw in adj[v]:
                if u not in shortest:
                    heapq.heappush(hp, (w+dw, u))
        
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        
        return shortest

