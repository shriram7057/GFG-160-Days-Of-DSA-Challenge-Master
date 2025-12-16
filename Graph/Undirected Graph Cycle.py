class Solution:
	def isCycle(self, V, edges):
		#Code here
		adj=[[]for _ in range(V)]
		for u,v in edges:
		    adj[u].append(v)
		    adj[v].append(u)
		visited=[False]*V
		
		def dfs(node,parent):
		    visited[node]=True
		    
		    for nei in adj[node]:
		        if not visited[nei]:
		            if dfs(nei,node):
		                return True
		        elif nei != parent:
		            return True
		    return False
		for i in range(V):
		    if not visited[i]:
		        if dfs(i,-1):
		            return True
		return False