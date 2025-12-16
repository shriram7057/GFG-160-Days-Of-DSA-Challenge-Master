class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here
        import heapq
        from collections import defaultdict
        
        adj= defaultdict(list)
        for u , v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
            
        INF = 10**18
        dist=[INF] * V
        dist[src] = 0
        
        pq=[(0,src)]
        
        while pq:
            d,node = heapq.heappop(pq)
            if d != dist[node]:
                continue
            for nei ,wt in adj[node]:
                if dist[nei] > d + wt:
                    dist[nei] = d+wt
                    heapq.heappush(pq,(dist[nei],nei))
        return dist