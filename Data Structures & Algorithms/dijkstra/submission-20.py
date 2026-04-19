class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {i:[] for i in range(n)}
        for u,v,w in edges:
            adj[u].append((v,w))
        
        shortest = {}

        hp = [(0, src)]

        while hp:
            w, u = heapq.heappop(hp)

            if u in shortest:
                continue
            
            shortest[u] = w

            for v,dw in adj[u]:
                
                if v not in shortest:

                    heapq.heappush(hp, (w+dw, v))


        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        
        return shortest

