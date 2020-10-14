# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def helper(head):
            if not head or not head.next:
                return head
            
            left, right = split(head)
            return merge(helper(left), helper(right))
        
        
        return helper(head)
        
        
def split(head):
    if not head:
        return head, head
    
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    mid = slow.next
    slow.next = None
    return head, mid


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
    