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
        
        line = [root]
        while line:
            for i in range(len(line) - 1):
                line[i].next = line[i + 1]
            
            next_line = []
            for node in line:
                if node.left:
                    next_line.append(node.left)
                if node.right:
                    next_line.append(node.right)
                    
            line = next_line
            
        return root
                
            
        