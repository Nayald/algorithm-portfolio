# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        l = deque()
        while head:
            next = head.next
            head.next = None
            l.append(head)
            head = next
            
        while len(l) > 1:
            l.append(merge(l.popleft(), l.popleft()))
            
        return l.popleft()
    
        
def merge(head1, head2):
    if not head1 or not head2:
        return head1 or head2
    
    dummy = ListNode(None)
    node = dummy
    node1 = head1
    node2 = head2
    while node1 and node2:
        if node1.val <= node2.val:
            node.next = node1
            node = node.next
            node1 = node1.next
        else:
            node.next = node2
            node = node.next
            node2 = node2.next
        
    node.next = node1 or node2
    return dummy.next