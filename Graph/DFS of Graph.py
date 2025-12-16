class Solution:
    def dfs(self, adj):
        # code 
        V=len(adj)
        visited=[False]*V
        ans=[]
        def dfsUtil(node):
            visited[node]=True
            ans.append(node)
            for nei in adj[node]:
                if not visited[nei]:
                    dfsUtil(nei)
        dfsUtil(0)
        return ans