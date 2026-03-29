class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {i: [] for i in range(n)}

        for u,v,w in edges:
            adj[u].append([v,w])
        
        minheap=[[0,src]]
        shortest = {}
        while minheap:
            w, x = heapq.heappop(minheap)

            if x in shortest:
                continue    
            
            shortest[x] = w

            for y, z in adj[x]:
                if y not in shortest:
                    heapq.heappush(minheap, [w+z, y])


        for i in range(n):
            if i not in shortest:
                shortest[i] = -1 
                
        
        return shortest


