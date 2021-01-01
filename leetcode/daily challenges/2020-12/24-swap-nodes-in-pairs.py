# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(None, head)
        p1 = dummy
        p2 = head
        while p2:
            n1 = p2.next
            if not n1:
                break
            
            p1.next = n1
            p2.next = n1.next
            n1.next = p2
            p1 = p2
            p2 = p2.next
            
        return dummy.next
            