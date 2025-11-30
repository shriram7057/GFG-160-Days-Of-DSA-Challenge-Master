"""
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""

class Solution:
    def reverseKGroup(self, head, k):
        # Code here
        if not head or k==1:
            return head
        dummy=Node(0)
        dummy.next=head
        prev=dummy
        
        while True:
            curr=prev.next
            tail=curr
            
            count=0
            temp=curr
            
            while temp and count < k:
                temp=temp.next
                count+=1
            if count < k:
                pass
            nxt=curr.next
            for _ in range(1,count):
                curr.next=nxt.next
                nxt.next=prev.next
                prev.next=nxt
                nxt=curr.next
            prev=curr
            if not nxt:
                break
        return dummy.next
                