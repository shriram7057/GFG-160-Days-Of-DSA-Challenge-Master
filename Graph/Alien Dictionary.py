from collections import defaultdict,deque
class Solution:
    def findOrder(self, words):
        # code here
        chars= set("".join(words))
        
        graph = defaultdict(list)
        indegree = {c: 0 for c in chars}
        
        for w1, w2 in zip(words,words[1:]):
            m, n = len(w1),len(w2)
            min_len=min(m,n)
            
            if m > n and w1.startswith(w2):
                return ""
            for i in range(min_len):
                if w1[i] != w2[i]:
                    graph[w1[i]].append(w2[i])
                    indegree[w2[i]] += 1
                    break
        q = deque([c for c in chars if indegree[c] == 0])
        order = []
        
        while q:
            u=q.popleft()
            order.append(u)
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        if len(order) != len(chars):
            return ""
        return "".join(order)