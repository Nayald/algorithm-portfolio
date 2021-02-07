# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        
        d = deque(lists)
        while len(d) > 1:
            l1 = d.popleft()
            l2 = d.popleft()
            d.append(merge(l1, l2))
            
        return d[0]
        
        
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