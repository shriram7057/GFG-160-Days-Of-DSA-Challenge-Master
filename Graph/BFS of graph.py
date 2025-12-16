class Solution:
    def bfs(self, adj):
        # code here
        V=len(adj)
        visited=[False]*V
        ans=[]
        q=deque()
        visited[0]=True
        q.append(0)
        while q:
            node=q.popleft()
            ans.append(node)
            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei]=True
                    q.append(nei)
        return ans
    