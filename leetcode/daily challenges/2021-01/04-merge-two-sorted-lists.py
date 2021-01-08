# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        l3 = ListNode(None)

        l1_pos = l1
        l2_pos = l2
        l3_pos = l3
        while l1_pos and l2_pos:
            if l1_pos.val <= l2_pos.val:
                l3_pos.next = l1_pos
                l1_pos = l1_pos.next
            else:
                l3_pos.next = l2_pos
                l2_pos = l2_pos.next
            l3_pos = l3_pos.next
            
        l3_pos.next = l1_pos or l2_pos

        return l3.next