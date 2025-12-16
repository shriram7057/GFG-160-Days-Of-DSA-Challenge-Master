class Solution:
    def findMinCycle(self, V, edges):
        # code here
        import heapq
        adj=[[] for _ in range(V)]
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
        INF = 10**18
        ans = INF

        for u,v,w in edges:
            dist=[INF] * V
            dist[u] = 0
            pq = [(0,u)]
            
            while pq:
                d, node = heapq.heappop(pq)
                if d > dist[node]:
                    continue
                for nei , wt in adj[node]:
                    if(node == u and nei == v) or (node == v and nei == u):
                        continue
                    if dist[nei] > d + wt:
                        dist[nei] = d + wt
                        heapq.heappush(pq,(dist[nei],nei))
            if dist[v] < INF:
                ans = min(ans,dist[v] + w)
        return ans if ans < INF else -1
                  