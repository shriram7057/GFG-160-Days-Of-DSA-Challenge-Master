#User function template for Python

class Solution:
	def floydWarshall(self, dist):
		#Code here
		n=len(dist)
		INF = 10 **8
		for k in range(n):
		    for i in range(n):
		        for j in range(n):
		            if dist[i][k] != INF and  dist[k][j] != INF:
		                if dist[i][k] + dist[k][j] < dist[i][j]:
		                    dist[i][j] = dist[i][k] + dist[k][j]
		                