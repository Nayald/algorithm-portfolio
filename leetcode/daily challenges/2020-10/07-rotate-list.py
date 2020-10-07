# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head
        
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
            
        n = k % length
        if n == 0:
            return head
        
        i = 0
        end = head
        while i < length - n - 1:
            end = end.next
            i += 1
        
        node = end
        while node.next:
            node = node.next
            
        node.next = head
        start = end.next
        end.next = None
        return start