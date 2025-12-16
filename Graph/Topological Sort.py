from collections import deque
class Solution:
    def topoSort(self, V, edges):
        # Code here
        adj=[[] for _ in range(V)]
        indeg=[0]*V
        for u , v in edges:
            adj[u].append(v)
            indeg[v] += 1
        q=deque()
        
        for i in range(V):
            if indeg[i] == 0:
                q.append(i)
        topo=[]
        
        while q:
            node=q.popleft()
            topo.append(node)
            
            for nxt in adj[node]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    q.append(nxt)
        return topo
            from collections import deque
class Solution:
    def topoSort(self, V, edges):
        # Code here
        adj=[[] for _ in range(V)]
        indeg=[0]*V
        for u , v in edges:
            adj[u].append(v)
            indeg[v] += 1
        q=deque()
        
        for i in range(V):
            if indeg[i] == 0:
                q.append(i)
        topo=[]
        
        while q:
            node=q.popleft()
            topo.append(node)
            
            for nxt in adj[node]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    q.append(nxt)
        return topo
            