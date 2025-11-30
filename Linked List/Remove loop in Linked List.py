'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''

class Solution:
    def removeLoop(self, head):
        # code here
        if not head or not head.next:
            return 
        slow=head
        fast=head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                break
        else:
            return 
        
        slow=head
        if slow==fast:
            
            while fast.next != slow:
                # slow=slow.next
                fast=fast.next
        else:
            while slow.next!=fast.next:
                slow=slow.next
                fast=fast.next
                
        fast.next=None