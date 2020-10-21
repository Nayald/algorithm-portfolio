"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
               
        graph = {}
        def explore(root):
            if root.val in graph:
                return graph[root.val]
            
            new_node = Node(root.val)
            graph[root.val] = new_node
            for neighbor in root.neighbors:
                new_node.neighbors.append(explore(neighbor))
            
            return new_node
            
        
        return explore(node)
