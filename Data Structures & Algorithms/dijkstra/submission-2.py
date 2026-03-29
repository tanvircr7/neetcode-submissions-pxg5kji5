class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {i: [] for i in range(n)}

        for u,v,w in edges:
            adj[u].append([v,w])
        
        minheap=[[0,src]]
        shortest = {}
        while minheap:
            d, u = heapq.heappop(minheap)
            print(f"d {d} - u {u}")

            if u in shortest:
                continue
            
            shortest[u] = d

            for v,w in adj[u]:
                if v not in shortest:
                    heapq.heappush(minheap, [d+w, v])

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1 
                
        
        return shortest


