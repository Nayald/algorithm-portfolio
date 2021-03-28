"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        head_copy = Node(head.val)
        curr_copy = head_copy
        curr = head
        d = {head: head_copy}
        while curr.next:
            curr_copy.next = Node(curr.next.val)
            curr_copy = curr_copy.next
            curr = curr.next
            d[curr] = curr_copy
            
        curr_copy = head_copy
        curr = head
        while curr:
            if curr.random:
                curr_copy.random = d[curr.random]
                
            curr_copy = curr_copy.next
            curr = curr.next
            
        return head_copy
            