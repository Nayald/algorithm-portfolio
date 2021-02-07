# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(None)
        head = l3
        
        carry = 0
        while l1 or l2:
            value = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            if value >= 10:
                value %= 10
                carry = 1
            else:
                carry = 0
                
            l3.next = ListNode(value)
            l3 = l3.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        if carry:
            l3.next = ListNode(1)
            
        return head.next
            
        