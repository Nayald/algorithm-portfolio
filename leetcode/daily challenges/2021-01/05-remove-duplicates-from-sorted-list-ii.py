# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        dummy = ListNode(None)
        dummy.next = head
        
        p1 = dummy
        p2 = head
        cpt = 1
        
        while p2:
            while p2.next and p2.val == p2.next.val:
                cpt += 1
                p2 = p2.next
                
            if cpt > 1:
                p1.next = p2.next
            else:
                p1 = p1.next
                
            p2 = p2.next
            cpt = 1
            
        return dummy.next