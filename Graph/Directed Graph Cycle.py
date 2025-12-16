from collections import deque,defaultdict
class Solution:
    def isCyclic(self, V, edges):
        # code here
        adj = defaultdict(list)
        
        for u , v in edges:
            adj[u].append(v)
        indeg=[0] * V
        for u in range(V):
            for v in adj[u]:
                indeg[v] += 1
        q=deque()
        for i in range(V):
            if indeg[i] == 0:
                q.append(i)
        count = 0 
        while q:
            node = q.popleft()
            count += 1
            
            for nei in adj[node]:
                indeg[nei] -= 1
                
                if indeg[nei] == 0:
                    q.append(nei)
        return count != V
            