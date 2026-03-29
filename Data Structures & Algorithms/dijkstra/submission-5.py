class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {i: [] for i in range(n)}
        for u,v,w in edges:
            adj[u].append([v,w])

        hp = [(0,src)]
        shortest = {}

        while hp:
            w, x = heapq.heappop(hp)
            if x in shortest:
                continue
            shortest[x] = w

            for y, dw in adj[x]:
                if y not in shortest:
                    heapq.heappush(hp, (w+dw, y))
            
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        
        return shortest


