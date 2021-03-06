# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                break
        
        if not fast or not fast.next:
            return None
        
        cycle = head
        while cycle is not slow:
            cycle = cycle.next
            slow = slow.next
            
        return cycle