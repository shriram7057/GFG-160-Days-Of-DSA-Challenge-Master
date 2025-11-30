'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.random = None
'''        

class Solution:
    def cloneLinkedList(self, head):
        # code here
        if head is None:
            return None
        curr=head
        while curr:
            new_node=Node(curr.data)
            new_node.next=curr.next
            curr.next=new_node
            curr=new_node.next
        curr=head
        while curr:
            if curr.random:
                curr.next.random=curr.random.next
            curr=curr.next.next
        curr=head
        cloned_head=head.next
        clone_curr=cloned_head
        
        while curr:
            curr.next=curr.next.next
            if clone_curr.next:
                clone_curr.next=clone_curr.next.next
            curr=curr.next
            clone_curr=clone_curr.next
        return cloned_head