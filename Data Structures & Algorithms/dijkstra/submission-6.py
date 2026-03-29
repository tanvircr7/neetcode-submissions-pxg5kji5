class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {i: [] for i in range(n)}
        for u,v,w in edges:
            adj[u].append([v,w])
        
        q = []
        heapq.heappush(q, [0,src])
        shortest = {}

        while q:
            w, r = heapq.heappop(q)

            if r in shortest:
                continue
            
            shortest[r] = w

            for c,dw in adj[r]:
                if c not in shortest:
                    heapq.heappush(q, [w+dw, c])
        
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        

        return shortest
