"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        q = deque([root, None])
        while q:
            node = q.popleft()
            if not node:
                if q:
                    q.append(None)
                    continue
                else:
                    break
            
            if node.left:
                q.append(node.left)
                
            if node.right:
                q.append(node.right)
                
            node.next = q[0]
            
        return root