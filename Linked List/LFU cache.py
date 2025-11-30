class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None
class LRUCache:
    def __init__(self,cap):
        self.cap=cap
        self.map={}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
    
    def _remove(self,node):
        p=node.prev
        n=node.next
        p.next=n
        n.prev=p
        
    def _add(self,node):
        p=self.tail.prev
        p.next=node
        node.prev=p
        node.next=self.tail
        self.tail.prev=node
    
    def get(self,key):
        if key not in self.map:
            return -1
        node=self.map[key]
        self._remove(node)
        self._add(node)
        return node.val
        
    def put(self,key,value):
        if key in self.map:
            self._remove(self.map[key])
        node=Node(key,value)
        self._add(node)
        self.map[key]=node
        
        if len(self.map)>self.cap:
            lru=self.head.next
            self._remove(lru)
            del self.map[lru.key]