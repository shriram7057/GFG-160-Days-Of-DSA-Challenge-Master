class Solution:
    def isBridge(self, V, edges, c, d):
        # code here 
        from collections import defaultdict
        adj= defaultdict(list)
        for u , v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited=[False] * V
        
        def dfs(node):
            visited[node]=True
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei)
        dfs(c)
        
        if not visited[d]:
            return 0
        adj[c].remove(d)
        adj[d].remove(c)
        
        visited=[False] * V
        dfs(c)
        return 1 if not visited[d] else 0