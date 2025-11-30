'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

'''
class Solution:
    def sortedMerge(self, head1, head2):
        # code here
        if not head1:
            return head2
        if not head2:
            return head1
        dummy=Node(0)
        tail=dummy
        while head1 and head2:
            if head1.data<=head2.data:
                tail.next=head1
                head1=head1.next
            else:
                tail.next=head2
                head2=head2.next
            tail=tail.next
        if head1:
            tail.next=head1
        else:
            tail.next=head2
        return dummy.next