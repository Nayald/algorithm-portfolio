# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        current = None
        next = l1
        while next:
            tmp = next.next
            next.next = current
            current = next
            next = tmp
            
        l1 = current
        
        current = None
        next = l2
        while next:
            tmp = next.next
            next.next = current
            current = next
            next = tmp
            
        l2 = current
        
        a = l1
        b = l2
        carry = 0
        head = ListNode(None)
        c = head
        while a or b or carry:
            if a:
                x = a.val
                a = a.next
            else:
                x = 0
            if b:
                y = b.val
                b = b.next
            else:
                y = 0
                
            r = x + y + carry
            if r >= 10:
                r -= 10
                carry = 1
            else:
                carry = 0
        
            c.next = ListNode(r)
            c = c.next
            
        current = None
        next = head.next
        while next:
            tmp = next.next
            next.next = current
            current = next
            next = tmp
            
        return current