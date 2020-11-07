# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        dummy = ListNode(float("-inf"))
        curr = head
        while curr:
            next = curr.next
            prev2 = dummy
            curr2 = dummy.next
            while curr2 and curr.val > curr2.val:
                prev2 = curr2
                curr2 = curr2.next

            prev2.next = curr
            curr.next = curr2
            curr = next
            
        return dummy.next
            
        